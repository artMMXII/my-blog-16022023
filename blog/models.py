from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
