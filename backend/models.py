# backend/models.py

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True, verbose_name='Телефон')
    directions = models.CharField(max_length=255, choices=[
        ("Boshlang'ich ta'lim", "Boshlang'ich ta'lim"),
        ("Tarix", "Tarix"),
        ("Filoligiya va tillarni o'qitish(O'zbek tili)", "Filoligiya va tillarni o'qitish(O'zbek tili)"),
        ("Filoligiya va tillarni o'qitish(Ingliz tili)", "Filoligiya va tillarni o'qitish(Ingliz tili)"),
        ],
        default="Boshlangich ta'lim"
    )
    education_type = models.CharField(max_length=20, choices=[
        ('full_time', 'Kunduzgi'),
        ('part_time', 'Sirtqi'),
        ],
        default='part_time'
    )
    status = models.BooleanField(default=False, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return self.full_name

class Qabul(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=20, unique=True)
    viloyat = models.CharField(max_length=255)
    tuman = models.CharField(max_length=255)
    mfy = models.CharField(max_length=255)
    kucha = models.CharField(max_length=255)
    uy = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255)
    attestat = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    father_address = models.CharField(max_length=255)
    father_job = models.CharField(max_length=255)
    father_phone_number = models.CharField(max_length=15)
    
    mother = models.CharField(max_length=255)
    mother_address = models.CharField(max_length=255)
    mother_job = models.CharField(max_length=255)
    mother_phone_number = models.CharField(max_length=15)
    directions = models.CharField(max_length=255, choices=[
        ("Boshlang'ich ta'lim", "Boshlang'ich ta'lim"),
        ("Tarix", "Tarix"),
        ("Filoligiya va tillarni o'qitish(O'zbek tili)", "Filoligiya va tillarni o'qitish(O'zbek tili)"),
        ("Filoligiya va tillarni o'qitish(Ingliz tili)", "Filoligiya va tillarni o'qitish(Ingliz tili)"),
        ],
        default="Boshlangich ta'lim"
    )
    education_type = models.CharField(max_length=20, choices=[
        ('full_time', 'Очное'),
        ('part_time', 'Заочное'),
    ])
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def address(self):
        return f'{self.viloyat}, {self.tuman}, {self.kucha}, uy-{self.uy}'
        
    class Meta:
        verbose_name = 'приём'
        verbose_name_plural = 'приём'

    def __str__(self):
        return self.full_name


class FileForDocuments(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    document = models.ForeignKey('Document', related_name='Document', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return f"File {self.pk}"

class Document(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name='*Заголовка(uz)')
    title_en = models.CharField(max_length=255, verbose_name='*Заголовка(en)')
    title_ru = models.CharField(max_length=255, verbose_name='*Заголовка(ru)')

    body_uz = RichTextField(max_length=255, verbose_name='Текст(uz)')
    body_en = RichTextField(max_length=255, verbose_name='Текст(en)')
    body_ru = RichTextField(max_length=255, verbose_name='Текст(ru)')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
    
    def __str__(self):
        return self.title_uz
    

class SertificateForEmployee(models.Model):
    queue = models.IntegerField(default=1, verbose_name='Очеред показа(Необязательно)')
    employee = models.ForeignKey('Employee', related_name='SertificateForEmployee', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sertificates/')

    def __str__(self):
        return f"Image {self.pk}"

class Employee(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='employee_photos/')

    full_name_uz = models.CharField(max_length=255, verbose_name='*ФИО(uz)')
    full_name_en = models.CharField(max_length=255, verbose_name='*ФИО(en)')
    full_name_ru = models.CharField(max_length=255, verbose_name='*ФИО(ru)')

    proffesion_uz = models.CharField(max_length=255, verbose_name='*Профессия(uz)')
    proffesion_en = models.CharField(max_length=255, verbose_name='*Профессия(en)')
    proffesion_ru = models.CharField(max_length=255, verbose_name='*Профессия(ru)')

    about_uz = RichTextField(verbose_name='*Инфо(uz)')
    about_en = RichTextField(verbose_name='*Инфо(en)')
    about_ru = RichTextField(verbose_name='*Инфо(ru)')

    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Почта')

    telegram = models.URLField(max_length=200, blank=True, null=True, verbose_name='Телеграм(https://t.me/username)')
    facebook = models.URLField(max_length=200, blank=True, null=True, verbose_name='Facebook(link)')
    instagram = models.URLField(max_length=200, blank=True, null=True, verbose_name='Инстаграм(link)')


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
    you_tube_video_link = models.URLField(max_length=255, blank=True, null=True)
    text_uz = RichTextField()
    text_en = RichTextField()
    text_ru = RichTextField()
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