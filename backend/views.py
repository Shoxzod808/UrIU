from django.shortcuts import render
from django.http import HttpResponse


def index(request, language='uz'):
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/home-1.html')
    else:
        return render(request, 'frontend/site/404.html')