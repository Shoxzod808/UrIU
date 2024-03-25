from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery, Category


def index(request, language='uz'):
    gallery_photos = Gallery.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
        'gallery_photos': gallery_photos,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/home-1.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def umumiy_malumot(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/umumiy_malumot.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def universitet_tarixi(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/universitet_tarixi.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rektor_tabrigi(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rektor_tabrigi.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def kengashlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/kengashlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def kafedralar(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/kafedralar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def fakultetlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/fakultetlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def markazlar_va_bolimlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/markazlar_va_bolimlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rektorat(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rektorat.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rekvizitlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rekvizitlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def qabul(request, language='uz'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'language': language,
    }
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/qabul.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)