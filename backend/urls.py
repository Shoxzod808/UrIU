from django.urls import path, include

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("<str:language>/", views.index, name="index"),
    path("", views.index, name="index"),
]

# Настройте обработку статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
