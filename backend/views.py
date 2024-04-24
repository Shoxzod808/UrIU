from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery, Category, News, Tag, Quote, Employee, SertificateForEmployee
from .models import Document, FileForDocuments
from django.http import JsonResponse
from django.core.paginator import Paginator



def index(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    gallery_photos = Gallery.objects.all()
    news = News.objects.all().order_by('-id')  # Сортирует новости начиная с последних
    if len(news) > 9:
        news = news[:9]
    quotes = Quote.objects.all()
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    context['quotes'] = quotes
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
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }

    context['language'] = language
    context['request'] = request
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/umumiy_malumot.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def universitet_tarixi(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }

    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/universitet_tarixi.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rektor_tabrigi(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }

    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rektor_tabrigi.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def kengashlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }

    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/kengashlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def kafedralar(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/kafedralar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def fakultetlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/fakultetlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def markazlar_va_bolimlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    tuzilma = Category.objects.get(name='Tuzilma')
    context['tuzilma'] = tuzilma
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/markazlar_va_bolimlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rtt(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    employees = [Employee.objects.get(id=10), Employee.objects.get(id=1), Employee.objects.get(id=3), Employee.objects.get(id=14)]
    context['employees'] = employees
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/RTT.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def meyoriy_hujjatlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    datas = Document.objects.all()
    documents = dict()
    for i in datas:
        documents[i.id] = FileForDocuments.objects.filter(document=i.id)
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    context['documents'] = documents
    context['datas'] = datas

    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/meyoriy_hujjatlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rektorat(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    employees = [Employee.objects.get(id=6), Employee.objects.get(id=4)]
    context['employees'] = employees
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rektorat.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def rekvizitlar(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/rekvizitlar.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def qabul(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/qabul.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def news(request, language='uz', page=1):
    categories = Category.objects.all()
    news = News.objects.all().order_by('-id')  # Сортирует новости начиная с последних
    context = {
            'categories': categories,
            'language': 'uz',
        }
    context['news'] = news
    context['request'] = request
    context['language'] = language
    context['prew2'] = None if page < 3 else page -2
    context['prew1'] = None if page == 1 else page-1
    context['current'] = page
    context['next1'] = page + 1
    context['next2'] = page + 2
    context['last'] = page + 10
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/news.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def coming_soon(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/coming_soon.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def contact(request, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    context['language'] = language
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/contact.html', context)
    else:
        context['language'] = 'uz'
        return render(request, '404.html', context)

def news_detail(request, news_id, language='uz'):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'language': 'uz',
        }
    
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
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

def employee_page(request, id, language='uz'):


    context = {
            'language': 'uz',
        }
    
    employee = Employee.objects.filter(id=id)
    if not employee.exists():
        context['language'] = language
        return render(request, '404.html', context)
    categories = Category.objects.all()
    employee = employee[0]
    sert = SertificateForEmployee.objects.filter(employee=employee).order_by('queue')

    context['sert'] = sert
    context['employee'] = employee
    context['categories'] = categories
    context['request'] = request
    context['language'] = language
    path = request.get_full_path()
    if path.split('/')[1] in ['ru', 'uz', 'en']:
        path = path[3:]
    path = path.rstrip('/')
    context['path'] = path
    if language in ['ru', 'en', 'uz']:
        return render(request, 'frontend/employee.html', context)
    else:
        context['language'] = language
        return render(request, '404.html', context)




