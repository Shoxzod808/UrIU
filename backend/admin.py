# backend/admin.py

from django.contrib import admin
from .models import News, Template, Template2Button, Gallery, Category, Button

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_en', 'body_ru', 'body_uz')
    search_fields = ('title', 'body_en', 'body_ru', 'body_uz')

@admin.register(Template2Button)
class Template2ButtonAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_en', 'body_ru', 'body_uz')
    search_fields = ('title', 'body_en', 'body_ru', 'body_uz')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'description_en', 'description_ru', 'description_uz', 'date', 'created']
    search_fields = ['description_en', 'description_ru', 'description_uz']
    list_filter = ['date', 'created']



class ButtonInline(admin.TabularInline):
    model = Button
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ButtonInline]

admin.site.register(Category, CategoryAdmin)
