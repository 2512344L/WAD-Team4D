from django.shortcuts import render

def index(request):
    return render(request, 'upskill_photography/index.html')
