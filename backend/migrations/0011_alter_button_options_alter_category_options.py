# Generated by Django 4.2.5 on 2024-03-25 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_button_link_alter_button_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='button',
            options={'verbose_name': 'кнопка', 'verbose_name_plural': 'кнопки'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'заголовка', 'verbose_name_plural': 'заголовки'},
        ),
    ]
