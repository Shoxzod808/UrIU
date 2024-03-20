# backend/admin.py

from django.contrib import admin
from .models import News, Template, Template2Button

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_en', 'body_ru', 'body_uz')
    search_fields = ('title', 'body_en', 'body_ru', 'body_uz')

@admin.register(Template2Button)
class Template2ButtonAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_en', 'body_ru', 'body_uz')
    search_fields = ('title', 'body_en', 'body_ru', 'body_uz')