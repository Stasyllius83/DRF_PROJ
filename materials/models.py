from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='materials/static/img', verbose_name='изображение', null=True, blank=True)
    description = models.TextField(max_length=250, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name='курс'
        verbose_name_plural='курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='materials/static/img', verbose_name='изображение', null=True, blank=True)
    description = models.TextField(max_length=250, verbose_name='описание')
    url = models.URLField(max_length=200, verbose_name='ссылка на видео', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='курс')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name='урок'
        verbose_name_plural='уроки'
