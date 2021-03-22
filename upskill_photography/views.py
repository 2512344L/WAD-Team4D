from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode, urlparse, parse_qs
from upskill_photography.models import Picture, Category
from django.views.generic import ListView

context_dict = {}
context_dict['categories'] = Category.objects.all

def index(request):
    context_dict = {}
    # Retrieve the 10 most liked pictures and add them to the context dict
    context_dict['pictures'] = Picture.objects.order_by('-likes')[:10]
    return render(request, 'upskill_photography/index.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'upskill_photography/about.html', context=context_dict)

def contact(request):
    context_dict = {}
    return render(request, 'upskill_photography/contact.html', context=context_dict)

def faq(request):
    context_dict = {}
    return render(request, 'upskill_photography/faq.html', context=context_dict)

def discovery(request):
    context_dict = {}
    return render(request, 'upskill_photography/discovery.html', context=context_dict)

def categories(request):
    context_dict = {}
    return render(request, 'upskill_photography/categories.html', context=context_dict)

def nature(request):
    context_dict = {}
    return render(request, 'upskill_photography/category_nature.html', context=context_dict)

def people(request):
    context_dict = {}
    return render(request, 'upskill_photography/category_people.html', context=context_dict)

def architecture(request):
    context_dict = {}
    return render(request, 'upskill_photography/category_architecture.html', context=context_dict)

def astronomy(request):
    context_dict = {}
    return render(request, 'upskill_photography/category_astronomy.html', context=context_dict)
def upload(request):
    context_dict={}
    return render(request, 'upskill_photography/upload.html', context=context_dict)
def search_result(request):
    if request.method == "POST":
        uploaded_file= request.FILES['document']
        query_text = request.POST.get('search_field', None)
        encoded_query_text = urlencode({'query':query_text})
        return redirect(f"/search/?{encoded_query_text}")
    else:
        query_text = (parse_qs(urlparse(request.build_absolute_uri()).query))['query'][0]
        keywords = query_text.split(' ')
        results = []
        context_dict = {}
        if len(results) != 0:
            context_dict['query'] = f"Showing results for '{query_text}'"
        else:
            context_dict['query'] = f"Could not find any results for '{query_text}'"
        return render(request, 'upskill_photography/search.html', context=context_dict)

@login_required
def account(request):
    context_dict = {}
    return render(request, 'upskill_photography/account.html', context=context_dict)

@login_required
def uploads(request):
    context_dict = {}
    return render(request, 'upskill_photography/uploads.html', context=context_dict)
