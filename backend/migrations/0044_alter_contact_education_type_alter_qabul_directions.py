# Generated by Django 5.0.3 on 2024-05-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0043_auto_20240524_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='education_type',
            field=models.CharField(choices=[('full_time', 'Kunduzgi'), ('part_time', 'Sirtqi')], default='part_time', max_length=20),
        ),
        migrations.AlterField(
            model_name='qabul',
            name='directions',
            field=models.CharField(choices=[("Boshlang'ich ta'lim", "Boshlang'ich ta'lim"), ('Tarix', 'Tarix'), ("Filoligiya va tillarni o'qitish(O'zbek tili)", "Filoligiya va tillarni o'qitish(O'zbek tili)"), ("Filoligiya va tillarni o'qitish(Ingliz tili)", "Filoligiya va tillarni o'qitish(Ingliz tili)")], default="Boshlangich ta'lim", max_length=255),
        ),
    ]