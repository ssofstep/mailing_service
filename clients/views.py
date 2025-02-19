from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Clients
from emailings.models import Mailing


class ClientsListView(ListView):
    model = Clients
    template_name = 'clients/clients_list.html'


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientForm
    template_name = 'clients/clients_form.html'
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientForm
    template_name = 'clients/clients_form.html'
    success_url = reverse_lazy('clients:clients_list')


class ClientsDetailView(DetailView):
    model = Clients


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


class HomeView(TemplateView):
    template_name = 'clients/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Mailing list management service"
        context_data["count_mailings"] = Mailing.objects.count()
        context_data["active_mailings_count"] = Mailing.objects.filter(
            status="started"
        ).count()
        unique_clients_count = Mailing.objects.values("recipients").distinct().count()
        context_data["unique_clients_count"] = unique_clients_count


        user = self.request.user
        user_mailings = Mailing.objects.filter(owner=user)
        context_data["all_sent_messages"] = (
                user_mailings.aggregate(Sum("all_sent_messages"))["all_sent_messages__sum"] or 0
        )
        context_data["unsuccessful_attempts"] = (
                user_mailings.aggregate(Sum("unsuccessful_attempts"))[
                    "unsuccessful_attempts__sum"
                ]
                or 0
        )
        context_data["successful_attempts"] = (
                user_mailings.aggregate(Sum("successful_attempts"))[
                    "successful_attempts__sum"
                ]
                or 0
        )


        return context_data