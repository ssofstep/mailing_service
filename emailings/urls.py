from django.urls import path

from emailings.views import MessageDeleteView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageListView, HomeView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('messages_list', MessageListView.as_view(), name='messages_list'),
    path('emailings/message_create', MessageCreateView.as_view(), name='message_create'),
    path('emailings/message_update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('emailings/message_detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('emailings/message_delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
]
