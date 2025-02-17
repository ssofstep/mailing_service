from django.db import models

from clients.models import Clients


class Message(models.Model):
    theme = models.CharField(verbose_name="Тема письма", max_length=150)
    body = models.TextField(verbose_name="Тело письма", blank=True, null=True)

    def __str__(self):
        return f'{self.theme} {self.body}'


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['theme']


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Завершена'),
        ('created', 'Создана'),
        ('started', 'Запущена'),
    ]

    start_datetime = models.DateTimeField(verbose_name="Дата и время первой отправки", blank=True, null=True)
    end_datetime = models.DateTimeField(verbose_name="Дата и время окончания отправки", blank=True, null=True)
    status = models.CharField(verbose_name="Статус", choices=STATUS_CHOICES, default='created', max_length=15)
    message = models.ForeignKey(Message, verbose_name="Сообщение", on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Clients, verbose_name="Получатели")

    def __str__(self):
        return f"{self.start_datetime} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["end_datetime"]


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ("status_ok", "Успешно"),
        ("status_nok", "Не успешно"),
    ]

    datetime_attempt = models.DateTimeField(verbose_name="Дата и время попытки")
    status = models.CharField(verbose_name="Статус", max_length=15, choices=STATUS_CHOICES)
    server_response = models.TextField(verbose_name="Ответ почтового сервера", blank=True, null=True)
    campaign = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name="Рассылка",
        related_name="mailing",
    )

    def __str__(self):
        return f"{self.datetime_attempt} <{self.status}>"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ["datetime_attempt", "status"]



