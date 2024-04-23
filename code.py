import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UrIU.settings")
django.setup()

from backend.models import Employee  # Импорт после настройки Django

# Изменение атрибута для всех объектов
for employee in Employee.objects.all():
    print(employee.photo)
