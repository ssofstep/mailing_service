from django.db import models

from users.models import CustomUser


class Clients(models.Model):
    email = models.EmailField(verbose_name="Почта клиента", unique=True)
    name = models.CharField(verbose_name="ФИО клиента", max_length=150)
    comment = models.TextField(verbose_name="Комментарий о клиенте", blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'{self.name} {self.email}'


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name', 'email']
