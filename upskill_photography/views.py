from django.shortcuts import render

def index(request):
    
    context_dict = {}
    
    return render(request, 'upskill_photography/index.html', context=context_dict)