# backend/models.py

from django.db import models

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