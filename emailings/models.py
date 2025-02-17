from django.db import models

class Message(models.Model):
    theme = models.CharField(verbose_name="Тема письма", max_length=150)
    body = models.TextField(verbose_name="Тело письма", blank=True, null=True)

    def __str__(self):
        return f'{self.theme} {self.body}'


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['theme']
