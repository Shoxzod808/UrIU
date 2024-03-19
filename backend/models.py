from django.db import models

class News(models.Model):  # Начинаем объявление модели "Новости"
    title = models.CharField(max_length=100)  # Поле для заголовка новости, тип данных CharField, максимальная длина 100 символов
    content = models.TextField()  # Поле для содержания новости, тип данных TextField

    def __str__(self):  # Метод для представления объекта модели в виде строки
        return self.title  # Возвращаем заголовок новости в качестве строки
