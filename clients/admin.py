from django.contrib import admin
from clients.models import Clients

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')
    search_fields = ('email', 'name')
