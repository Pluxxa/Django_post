from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField('Имя', max_length=20, default='default_name')
    title = models.CharField('Пост', max_length=50)
    short_decr = models.CharField('Краткое содержание', max_length=200)
    text = models.TextField('Информация')
    put_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'