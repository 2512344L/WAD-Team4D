from django.shortcuts import render

def index(request):
    context_dict = {}
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

def search_result(request):
    context_dict = {}
    return render(request, 'upskill_photography/search.html', context=context_dict)
