from django.urls import path

from clients.views import ClientsListView, ClientsCreateView, ClientsDetailView, ClientsDeleteView, ClientsUpdateView, \
    HomeView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clients_list', ClientsListView.as_view(), name='clients_list'),
    path('clients/client_create', ClientsCreateView.as_view(), name='client_create'),
    path('clients/client_update/<int:pk>', ClientsUpdateView.as_view(), name='client_update'),
    path('clients/client_detail/<int:pk>', ClientsDetailView.as_view(), name='client_detail'),
    path('clients/client_delete/<int:pk>', ClientsDeleteView.as_view(), name='client_delete'),
]
