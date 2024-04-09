# backend/admin.py

from django.contrib import admin
from .models import News, Template, Template2Button, Gallery, Category, Button, Tag, GalleryForNews
from .models import Quote, Employee, SertificateForEmployee, Document, FileForDocuments

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'text_uz')

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

class GalleryForNewsInline(admin.TabularInline):
    model = GalleryForNews
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [GalleryForNewsInline]
    filter_horizontal = ('tags',)

admin.site.register(News, NewsAdmin)
admin.site.register(Tag)

class SertificateForEmployeeInline(admin.TabularInline):
    model = SertificateForEmployee
    extra = 1  # Количество форм для добавления новых сертификатов

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_uz', 'proffesion_uz', 'phone', 'email')  # Поля, которые будут отображаться в списке
    search_fields = ('full_name_uz', 'proffesion_uz')  # Поля, по которым будет работать поиск
    inlines = [SertificateForEmployeeInline, ]

    # Если вы хотите добавить фильтрацию по полям, используйте list_filter
    # list_filter = ('proffesion_uz',)

admin.site.register(Employee, PeopleAdmin)

class FileForDocumentsInline(admin.TabularInline):
    model = FileForDocuments
    extra = 1  # Количество форм для добавления новых сертификатов

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'body_uz')  # Поля, которые будут отображаться в списке
    search_fields = ('title_uz',)  # Поля, по которым будет работать поиск
    inlines = [FileForDocumentsInline, ]

    # Если вы хотите добавить фильтрацию по полям, используйте list_filter
    # list_filter = ('proffesion_uz',)

admin.site.register(Document, DocumentAdmin)