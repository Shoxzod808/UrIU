# Generated by Django 5.0.3 on 2024-05-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0045_merge_20240524_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qabul',
            old_name='address',
            new_name='kucha',
        ),
        migrations.AddField(
            model_name='qabul',
            name='mfy',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qabul',
            name='tuman',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qabul',
            name='uy',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qabul',
            name='viloyat',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]