from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='materials/static/img', verbose_name='изображение', **NULLABLE)
    discription = models.CharField(max_length=250, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.discription}'

    class Meta:
        verbose_name='курс'
        verbose_name_plural='курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='materials/static/img', verbose_name='изображение', **NULLABLE)
    discription = models.CharField(max_length=250, verbose_name='описание')
    url = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.name} {self.discription}'

    class Meta:
        verbose_name='урок'
        verbose_name_plural='уроки'
