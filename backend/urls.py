from django.urls import path, include

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.shortcuts import redirect

def default_language_redirect(request):
    return redirect('index', language='uz')

urlpatterns = [
    path('', default_language_redirect),
    path("info/", views.info, name="info"),
    path("<str:language>/coming_soon", views.coming_soon, name="coming_soon"),
    path("<str:language>/news-<int:page>", views.news, name="news"),
    path("<str:language>/employee-<int:id>/", views.employee_page, name="employee"),
    path("<str:language>/news/", views.news, name="news"),
    path("<str:language>/contact/", views.contact, name="contact"),
    path("<str:language>/", views.index, name="index"),
    path("<str:language>/news/<int:news_id>", views.news_detail, name="news_detail"),
    path("<str:language>/rektor_tabrigi/", views.rektor_tabrigi, name="rektor_tabrigi"),
    path("<str:language>/meyoriy_hujjatlar/", views.meyoriy_hujjatlar, name="meyoriy_hujjatlar"),
    path("<str:language>/umumiy_malumot/", views.umumiy_malumot, name="umumiy_malumot"),
    path("<str:language>/universitet_tarixi/", views.universitet_tarixi, name="universitet_tarixi"),
    path("<str:language>/rektor_tabrigi/", views.rektor_tabrigi, name="rektor_tabrigi"),
    path("<str:language>/kengashlar/", views.kengashlar, name="kengashlar"),
    path("<str:language>/kafedralar/", views.kafedralar, name="kafedralar"),
    path("<str:language>/fakultetlar/", views.fakultetlar, name="fakultetlar"),
    path("<str:language>/markazlar_va_bolimlar/", views.markazlar_va_bolimlar, name="markazlar_va_bolimlar"),
    path("<str:language>/markazlar_va_bolimlar/rtt", views.rtt, name="rtt"),
    path("<str:language>/rektorat/", views.rektorat, name="rektorat"),
    path("<str:language>/rekvizitlar/", views.rekvizitlar, name="rekvizitlar"),
    path("<str:language>/qabul/", views.qabul, name="qabul"),
    
]


# Настройте обработку статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
