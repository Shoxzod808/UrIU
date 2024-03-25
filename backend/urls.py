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
    path("<str:language>/", views.index, name="index"),
]


# Настройте обработку статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
