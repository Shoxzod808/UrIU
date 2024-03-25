# backend/models.py

from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'заголовка'
        verbose_name_plural = 'заголовки'

    def __str__(self):
        return self.name

class Button(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'кнопка'
        verbose_name_plural = 'кнопки'

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
    def __str__(self):
        return self.name

class GalleryForNews(models.Model):
    news = models.ForeignKey('News', related_name='gallery_for_news', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_gallery/')

    def __str__(self):
        return f"Image {self.pk}"

class News(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news_photos/')
    text_uz = models.TextField()
    text_en = models.TextField()
    text_ru = models.TextField()
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title_uz


class Template(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Ключь')
    body_en = models.TextField(verbose_name='English')
    body_ru = models.TextField(verbose_name='Русский')
    body_uz = models.TextField(verbose_name='Uzbekcha')

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    def __str__(self):
        return self.title

class Template2Button(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Ключь')
    body_en = models.TextField(verbose_name='English')
    body_ru = models.TextField(verbose_name='Русский')
    body_uz = models.TextField(verbose_name='Uzbekcha')

    class Meta:
        verbose_name = 'Небольшой шаблон'
        verbose_name_plural = 'Небольшие шаблоны'

    def __str__(self):
        return self.title

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery_photos/')
    description_en = models.TextField(null=True, blank=True, verbose_name='English')
    description_ru = models.TextField(null=True, blank=True, verbose_name='Русский')
    description_uz = models.TextField(null=True, blank=True, verbose_name='Uzbekcha')
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return f'Gallery #{self.id}'