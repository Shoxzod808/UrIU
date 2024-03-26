from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery, Category, News, Tag


categories = Category.objects.all()
context = {
        'categories': categories,
        'language': 'uz',
    }

def index(request, language='uz'):
    global context
    gallery_photos = Gallery.objects.all()
    news = News.objects.all()
    context['language'] = language
    context['request'] = request
    context['gallery_photos']: gallery_photos
    context['news'] = news
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/home-1.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def umumiy_malumot(request, language='uz'):
    global context

    context['language'] = language
    context['request'] = request

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/umumiy_malumot.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def universitet_tarixi(request, language='uz'):
    global context

    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/universitet_tarixi.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rektor_tabrigi(request, language='uz'):
    global context

    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rektor_tabrigi.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def kengashlar(request, language='uz'):
    global context

    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/kengashlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def kafedralar(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/kafedralar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def fakultetlar(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/fakultetlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def markazlar_va_bolimlar(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/markazlar_va_bolimlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rektorat(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rektorat.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rekvizitlar(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rekvizitlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def qabul(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/qabul.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def news(request, language='uz'):
    global context
    
    context['request'] = request
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/news.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def contact(request, language='uz'):
    global context
    
    context['language'] = language

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/contact.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def news_detail(request, news_id, language='uz'):
    global context
    

    tags = Tag.objects.all()
    news_item = News.objects.get(id=news_id)
    context['request'] = request
    context['language'] = language
    context['news_item'] = news_item
    context['tags'] = tags

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/news_detail.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)