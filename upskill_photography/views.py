from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode, urlparse, parse_qs

from .models import Picture
from django.core.files.storage import FileSystemStorage
from upskill_photography.models import Picture, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import uploading
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from upskill_photography.models import Picture, Category
from django.views.generic import ListView

# Initialize the Context dict and add the categories to it by default
context_dict = {}
context_dict['categories'] = Category.objects.all

# Initialize the Query String dict
query_dict = {}

# This should be called whenever we want to extract parameters from the request url string
def get_query_parameters(request):
    if request.method == "GET":
        url_params = parse_qs(urlparse(request.build_absolute_uri()).query)
        for param in url_params:
            query_dict[param] = url_params[param][0]
            
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
    context_dict['pictures'] = Picture.objects.order_by('-likes')[:10]
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
        get_query_parameters(request)
        pictures = Picture.objects.order_by('-timestamp')
        
        if pictures and 'sort' in query_dict:
            sort_style, sort_order = query_dict['sort'].split('_')
            pictures = picture_ordering(pictures, sort_style, sort_order)   
            context_dict['sort_style'] = sort_style
            context_dict['sort_order'] = sort_order
        
        context_dict['pictures'] = pictures
        return render(request, 'upskill_photography/discovery.html', context=context_dict)


def categories(request):
    return render(request, 'upskill_photography/categories.html', context=context_dict)


def show_category(request, category_name_slug):
    # Pictures can have sort order
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
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
        get_query_parameters(request)
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
    return render(request, 'upskill_photography/user_profile.html', context=context_dict)


def picture_view(request, userprofile_username, picture_id):
    return render(request, 'upskill_photography/picture_view.html', context=context_dict)


@login_required
def account(request):
    return render(request, 'upskill_photography/account.html', context=context_dict)


@login_required
def uploads(request):
    return render(request, 'upskill_photography/uploads.html', context=context_dict)

@login_required
def upload(request):
    return render(request, 'upskill_photography/upload.html', context=context_dict)


class postlistview(ListView):
    model = Picture
    template_name = 'upskill_photography/index.html'
    context_object_name = 'picture'
    ordering = ['timestamp']


class postDetailView(DetailView):
    model = Picture


class postDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Picture
    success_url = '/'


class postCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    fields = ['Title', 'image']

    def form_valid(self, form):
        form.instance.uploading_user = self.request.user
        return super().form_valid(form)


class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Picture
    fields = ['Title', 'image']

    def form_valid(self, form):
        form.instance.uploading_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == Picture.uploading_user:
            return True
        return False
