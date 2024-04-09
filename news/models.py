from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class AllObject(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='юзер')
    title = models.CharField(verbose_name='название', max_length=128)
    img = models.ImageField(verbose_name='картинка', upload_to='images/')
    des = models.TextField(verbose_name='текст')
    address = models.CharField(max_length=128, verbose_name='адресс')
    price = models.CharField(verbose_name='цена', max_length=32)
    max_human = models.IntegerField(verbose_name='макс. кол-во человек')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'