# Generated by Django 4.2.5 on 2024-03-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_news_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('short_text_uz', models.CharField(max_length=255)),
                ('short_text_ru', models.CharField(max_length=255)),
                ('short_text_en', models.CharField(max_length=255)),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
                ('text_en', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
    ]