from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from upskill_photography.models import Picture, UserProfile, User, Category, Comment
from urllib.parse import urlencode, urlparse, parse_qs

from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import UploadFileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView

# Initialize the Context dict and add the categories to it by default
context_dict = {}
context_dict['categories'] = list(Category.objects.all())


# This should be called whenever we want to extract parameters from the request url string
def get_query_parameters(request):
    query_dict = {}
    if request.method == "GET":
        url_params = parse_qs(urlparse(request.build_absolute_uri()).query)
        for param in url_params:
            query_dict[param] = url_params[param][0]
    return query_dict

## Private Method ##
def picture_ordering(pictures, sort_style, sort_order):
    def upload_time(picture):
        return picture.timestamp

    def views(picture):
        return picture.views

    def likes(picture):
        return picture.likes

    pictures = list(pictures)

    reverse = True
    if sort_order == "asc":
        reverse = False

    func = upload_time
    if sort_style == "views":
        func = views
    elif sort_style == "likes":
        func = likes

    pictures.sort(reverse=reverse, key=func)
    return pictures


def index(request):
    # Retrieve the 10 most liked pictures and add them to the context dict
    context_dict['first_picture'] = list(Picture.objects.order_by('-likes'))[0]
    context_dict['pictures'] = list(Picture.objects.order_by('-likes'))[1:10]
    context_dict['counter'] = list(range(1, len(context_dict['pictures']) + 1))
    return render(request, 'upskill_photography/index.html', context=context_dict)


def about(request):
    return render(request, 'upskill_photography/about.html', context=context_dict)


def contact(request):
    return render(request, 'upskill_photography/contact.html', context=context_dict)


def faq(request):
    return render(request, 'upskill_photography/faq.html', context=context_dict)


def discovery(request):
    if request.method == "POST":
        query_string = {}

        sort_style = request.POST.get('sort_style', "")
        sort_order = request.POST.get('sort_order', "")
        if sort_style != "" and sort_order != "":
            query_string['sort'] = sort_style + "_" + sort_order

        if len(query_string) > 0:
            encoded_query_string = urlencode(query_string)
            return redirect(reverse('upskill_photography:discovery') + f"?{encoded_query_string}")
        else:
            return redirect(reverse('upskill_photography:discovery'))
    else:
        query_dict = get_query_parameters(request)
        pictures = Picture.objects.order_by('-timestamp')

        if pictures and 'sort' in query_dict:
            sort_style, sort_order = query_dict['sort'].split('_')
            pictures = picture_ordering(pictures, sort_style, sort_order)
            context_dict['sort_style'] = sort_style
            context_dict['sort_order'] = sort_order
        else:
            context_dict['sort_style'] = "new"
            context_dict['sort_order'] = "desc"

        context_dict['pictures'] = pictures
        return render(request, 'upskill_photography/discovery.html', context=context_dict)


def categories(request):
    pictures = []
    for category in context_dict['categories']:
        pictures = pictures + list(Picture.objects.filter(category=Category.objects.get(name=category.name)).order_by('-likes'))[0:1]
    context_dict['pictures'] = pictures
    return render(request, 'upskill_photography/categories.html', context=context_dict)


def show_category(request, category_name_slug):
    if request.method == "POST":
        query_string = {}
        
        sort_style = request.POST.get('sort_style', "")
        sort_order = request.POST.get('sort_order', "")
        if sort_style != "" and sort_order != "":
            query_string['sort'] = sort_style + "_" + sort_order
        
        if len(query_string) > 0:
            encoded_query_string = urlencode(query_string)
            return redirect(reverse('upskill_photography:show_category', kwargs={'category_name_slug': category_name_slug}) + f"?{encoded_query_string}")
        else:
            return redirect(reverse('upskill_photography:show_category', kwargs={'category_name_slug': category_name_slug}))
    else:
        query_dict = get_query_parameters(request)
        pictures = []
        try:
            category = Category.objects.get(slug=category_name_slug)
            pictures = list(Picture.objects.filter(category=Category.objects.get(slug=category_name_slug)).order_by('-timestamp'))
            context_dict['category'] = category
        except Category.DoesNotExist:
            context_dict['category'] = None
            pictures = None
        
        if pictures and 'sort' in query_dict:
            sort_style, sort_order = query_dict['sort'].split('_')
            pictures = picture_ordering(pictures, sort_style, sort_order)   
            context_dict['sort_style'] = sort_style
            context_dict['sort_order'] = sort_order
        else:
            context_dict['sort_style'] = "new"
            context_dict['sort_order'] = "desc"
        
        context_dict['pictures'] = pictures
        return render(request, 'upskill_photography/category.html', context=context_dict)


def search_result(request):
    if request.method == "POST":
        query_string = {}

        query_text = request.POST.get('search_query', None)
        if query_text:
            query_string['query'] = query_text

        sort_style = request.POST.get('sort_style', "")
        sort_order = request.POST.get('sort_order', "")
        if sort_style != "" and sort_order != "":
            query_string['sort'] = sort_style + "_" + sort_order

        if len(query_string) > 0:
            encoded_query_string = urlencode(query_string)
            return redirect(reverse('upskill_photography:search_result') + f"?{encoded_query_string}")
        else:
            return redirect(reverse('upskill_photography:search_result'))
    else:
        query_dict = get_query_parameters(request)
        query_text = ""
        if 'query' in query_dict:
            query_text = query_dict['query']

        results = search_function(query_text)

        context_dict['sort_style'] = "relevance"
        context_dict['sort_order'] = "relevance"
        if results and 'sort' in query_dict:
            sort_style, sort_order = query_dict['sort'].split('_')
            results = picture_ordering(results, sort_style, sort_order)
            context_dict['sort_style'] = sort_style
            context_dict['sort_order'] = sort_order

        context_dict['results'] = results
        context_dict['query'] = query_text
        return render(request, 'upskill_photography/search.html', context=context_dict)

## Private Method ##
def search_function(query_text):
    results = []
    keywords = query_text.lower().split(' ')

    # Remove any unnecessary keywords from the keyword list
    obsolete_keywords = ['a', 'an', 'and', 'the', '&']
    for obsolete_keyword in obsolete_keywords:
        while obsolete_keyword in keywords:
            keywords.remove(obsolete_keyword)

    # First search for similarities with the whole query text
    results = results + list(Picture.objects.filter(title__icontains=query_text))

    # Then search for similarities with each keyword
    for keyword in keywords:
        results = results + list(Picture.objects.filter(title__icontains=keyword))

    if len(results) != 0:
        results = list(dict.fromkeys(results))  # To make the results unique
    else:
        results = None
    return results


def userprofile(request, userprofile_username):
    try:
        user = User.objects.get(username=userprofile_username)
        context_dict['user'] = UserProfile.objects.get(user=user)
    except (User.DoesNotExist, UserProfile.DoesNotExist):
        context_dict['user'] = None
    return render(request, 'upskill_photography/user_profile.html', context=context_dict)


def picture_view(request, userprofile_username, picture_id):
    if request.method == "POST":
        comment_username = request.POST.get('comment_username', None)
        comment_text = request.POST.get('comment_text', None)
        picture = None
        user = None
        try:
            picture = Picture.objects.get(picture_id=picture_id)
            user = UserProfile.objects.get(user=User.objects.get(username=comment_username))
        except Picture.DoesNotExist:
            pass
        except (UserProfile.DoesNotExist, User.DoesNotExist):
            pass
        if user and comment_text and picture:
            comment = Comment(picture=picture, user=user, text=comment_text)
            comment.save()
        return redirect(reverse('upskill_photography:picture_view', kwargs={'userprofile_username': userprofile_username, 'picture_id': picture_id}))
    else:
        try:
            picture = Picture.objects.get(picture_id=picture_id)
            comments = Comment.objects.filter(picture=picture).order_by('-timestamp')
            picture.views = picture.views + 1
            picture.save()
            more_pictures = list(Picture.objects.filter(uploading_user=picture.uploading_user).order_by('-likes'))[0:10]
            context_dict['picture'] = picture
            context_dict['comments'] = comments
            context_dict['more_pictures'] = more_pictures
        except Picture.DoesNotExist:
            context_dict['picture'] = None
        return render(request, 'upskill_photography/picture_view.html', context=context_dict)


@login_required
def account(request):
    return render(request, 'upskill_photography/account.html', context=context_dict)


@login_required
def uploads(request):
    return render(request, 'upskill_photography/uploads.html', context=context_dict)


@login_required
def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES('document')
        fs = FileSystemStorage
        name=fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upskill_photography/upload.html', context=context)


# Handles AJAX requests for liking pictures
class LikePictureView(View):
    @method_decorator(login_required)
    def get(self, request):
        picture_id = request.GET['picture_id']
        picture = None
        try:
            picture = Picture.objects.get(picture_id=picture_id)
        except Picture.DoesNotExist:
            return HttpResponse(-1)
         
        picture.likes = picture.likes + 1
        picture.save()
        return HttpResponse(picture.likes)


# Handles AJAX requests for removing comments
class RemoveCommentView(View):
    @method_decorator(login_required)
    def get(self, request):
        comment_id = request.GET['comment_id']
        try:
            Comment.objects.get(id=comment_id).delete()
        except Comment.DoesNotExist:
            return HttpResponse(-1)
        return HttpResponse(0);