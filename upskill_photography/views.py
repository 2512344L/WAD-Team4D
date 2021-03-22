from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode, urlparse, parse_qs
from django.core.files.storage import FileSystemStorage
from upskill_photography.models import Picture, Category
from django.views.generic import ListView

context_dict = {}
context_dict['categories'] = Category.objects.all

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
    return render(request, 'upskill_photography/discovery.html', context=context_dict)

def categories(request):
    return render(request, 'upskill_photography/categories.html', context=context_dict)

def show_category(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
    return render(request, 'upskill_photography/category.html', context=context_dict)

def search_result(request):
    if request.method == "POST":
        query_text = request.POST.get('search_field', None)
        encoded_query_text = urlencode({'query':query_text})
        return redirect(f"/search/?{encoded_query_text}")
    else:
        query_text = (parse_qs(urlparse(request.build_absolute_uri()).query))['query'][0]
        keywords = query_text.lower().split(' ')
        
        # Remove any unnecessary keywords from the keyword list
        obsolete_keywords = ['a', 'an', 'and', 'the', '&']
        for obsolete_keyword in obsolete_keywords:
            while obsolete_keyword in keywords:
                keywords.remove(obsolete_keyword)
        
        results = []
        
        # First search for similarities with the whole query text
        results = results + list(Picture.objects.filter(title__icontains=query_text))
        
        # Then search for similarities with each keyword
        for keyword in keywords:
            results = results + list(Picture.objects.filter(title__icontains=keyword))     

        if len(results) != 0:
            context_dict['query'] = f"Showing results for '{query_text}'"
            context_dict['results'] = list(dict.fromkeys(results)) # To make the results unique
        else:
            context_dict['query'] = f"Could not find any results for '{query_text}'"
            context_dict['results'] = None
        return render(request, 'upskill_photography/search.html', context=context_dict)

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
    if request.method == 'POST':
        uploaded_file = request.files['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context_dict['url'] = fs.url(name)
    return render(request, 'upskill_photography/upload.html', context=context_dict)