from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(null= False, blank=False, upload_to='images', verbose_name='Фото')
    caption = models.CharField(max_length=200, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    likes = models.IntegerField(default=0, verbose_name='Количество лайков')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos', verbose_name='Автор')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

class Comment(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    photo = models.ForeignKey('webapp.Photo', related_name='comments', on_delete=models.CASCADE, verbose_name='Фото')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

