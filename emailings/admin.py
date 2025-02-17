from django.contrib import admin

from emailings.models import Message, Mailing


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'body')
    search_fields = ('theme', 'body')



@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_datetime', 'end_datetime', 'status')
    search_fields = ('status',)
