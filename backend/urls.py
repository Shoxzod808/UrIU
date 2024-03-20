from django.urls import path, include

from . import views

urlpatterns = [
    path("<str:language>/", views.index, name="index"),
    path("", views.index, name="index"),
]
