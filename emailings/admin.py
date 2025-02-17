from django.contrib import admin

from emailings.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'body')
    search_fields = ('theme', 'body')
