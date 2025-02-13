from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Clients


class ClientsListView(ListView):
    model = Clients
    template_name = 'clients/client_list.html'


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientForm
    template_name = 'clients/clients_form.html'
    success_url = reverse_lazy('clients:client_list')


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientForm
    template_name = 'clients/clients_form.html'
    success_url = reverse_lazy('clients:client_list')


class ClientsDetailView(DetailView):
    model = Clients


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:client_list')


class HomeView(TemplateView):
    template_name = 'clients/home.html'
