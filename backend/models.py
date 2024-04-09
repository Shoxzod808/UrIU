# backend/models.py

from django.db import models
from django.utils import timezone




class SertificateForEmployee(models.Model):
    employee = models.ForeignKey('Employee', related_name='SertificateForEmployee', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sertificates/')

    def __str__(self):
        return f"Image {self.pk}"

class Employee(models.Model):
    photo = models.ImageField(upload_to='*employee_photos/')

    full_name_uz = models.CharField(max_length=255, verbose_name='*ФИО(uz)')
    full_name_en = models.CharField(max_length=255, verbose_name='*ФИО(en)')
    full_name_ru = models.CharField(max_length=255, verbose_name='*ФИО(ru)')

    proffesion_uz = models.CharField(max_length=255, verbose_name='*Профессия(uz)')
    proffesion_en = models.CharField(max_length=255, verbose_name='*Профессия(en)')
    proffesion_ru = models.CharField(max_length=255, verbose_name='*Профессия(ru)')

    about_uz = models.TextField(max_length=255, verbose_name='*Инфо(uz)')
    about_en = models.TextField(max_length=255, verbose_name='*Инфо(en)')
    about_ru = models.TextField(max_length=255, verbose_name='*Инфо(ru)')

    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Почта')

    telegram = models.URLField(max_length=200, blank=True, null=True, verbose_name='Телеграм')
    facebook = models.URLField(max_length=200, blank=True, null=True, verbose_name='Facebook')
    instagram = models.URLField(max_length=200, blank=True, null=True, verbose_name='Инстаграм')


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    
    def __str__(self):
        return self.full_name_uz



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

class Quote(models.Model):
    photo = models.ImageField(upload_to='gallery_photos/')

    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    short_text_uz = models.CharField(max_length=255)
    short_text_ru = models.CharField(max_length=255)
    short_text_en = models.CharField(max_length=255)

    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'цитата'
        verbose_name_plural = 'цитаты'
    
    def __str__(self):
        return self.name_uz