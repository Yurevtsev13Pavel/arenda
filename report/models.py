from django.contrib.auth.models import User
from django.db import models

from news.models import AllObject


# Create your models here.
class Report(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='юзер')
    object_id = models.ForeignKey(AllObject, on_delete=models.CASCADE, verbose_name='ид')
    comment = models.TextField(verbose_name='текст')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def str(self):
        return self.comment

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

