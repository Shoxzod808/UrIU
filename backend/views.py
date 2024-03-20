from django.shortcuts import render
from django.http import HttpResponse


def index(request, language='uz'):
    if language in ['ru', 'en', 'uz']:
        context = {
            'language': language
        }
        return render(request, 'frontend/home-1.html', context)
    else:
        return render(request, 'frontend/404.html')