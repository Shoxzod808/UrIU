from django.contrib import admin
from .models import News
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'content',)
    search_fields = ('title', 'content',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content',)
        }),
    )

admin.site.register(News, NewsAdmin)
