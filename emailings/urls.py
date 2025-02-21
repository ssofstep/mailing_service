from django.urls import path
from django.views.decorators.cache import cache_page

from emailings.views import (MessageDeleteView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageListView, HomeView,
                             MailingCreateView, MailingDeleteView, MailingUpdateView, MailingDetailView, MailingListView)

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('messages_list', cache_page(60)(MessageListView.as_view()), name='messages_list'),
    path('emailings/message_create', MessageCreateView.as_view(), name='message_create'),
    path('emailings/message_update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('emailings/message_detail/<int:pk>', cache_page(60)(MessageDetailView.as_view()), name='message_detail'),
    path('emailings/message_delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('mailings_list', cache_page(60)(MailingListView.as_view()), name='mailings_list'),
    path('emailings/mailing_create', MailingCreateView.as_view(), name='mailing_create'),
    path('emailings/mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('emailings/mailing_detail/<int:pk>', cache_page(60)(MailingDetailView.as_view()), name='mailing_detail'),
    path('emailings/mailing_delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
]
