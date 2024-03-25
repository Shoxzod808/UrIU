# backend/models.py

from django.db import models

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


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

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