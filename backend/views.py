from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery


def index(request, language='uz'):
    gallery_photos = Gallery.objects.all()
    context = {
        'language': language,
        'gallery_photos': gallery_photos,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/home-1.html', context)
    else:
        context['language'] = 'uz'
        return render(request, 'frontend/404.html', context)