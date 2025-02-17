from django.urls import path

from emailings.views import MessageDeleteView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageListView, HomeView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('emailings_list', MessageListView.as_view(), name='emailings_list'),
    path('emailings/emailing_create', MessageCreateView.as_view(), name='emailing_create'),
    path('emailings/emailing_update/<int:pk>', MessageUpdateView.as_view(), name='emailing_update'),
    path('emailings/emailing_detail/<int:pk>', MessageDetailView.as_view(), name='emailing_detail'),
    path('emailings/emailing_delete/<int:pk>', MessageDeleteView.as_view(), name='emailing_delete'),
]
