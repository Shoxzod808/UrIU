from django.shortcuts import render
from django.http import HttpResponse


def index(request, language='uz'):
    context = {
        'language': language
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/home-1.html', context)
    else:
        context['language'] = 'uz'
        return render(request, 'frontend/404.html', context)