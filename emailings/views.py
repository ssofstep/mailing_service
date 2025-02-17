from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from emailings.forms import MessageForm, MailingForm
from emailings.models import Message, Mailing


class MessageListView(ListView):
    model = Message
    template_name = 'emailings/messages_list.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'emailings/messages_form.html'
    success_url = reverse_lazy('emailings:messages_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'emailings/messages_form.html'
    success_url = reverse_lazy('emailings:messages_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'emailings/messages_detail.html'


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'emailings/messages_confirm_delete.html'
    success_url = reverse_lazy('emailings:messages_list')


class HomeView(TemplateView):
    template_name = 'emailings/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Mailing list management service"
        context_data["count_mailing"] = Mailing.objects.count()
        context_data["active_mailing_count"] = Mailing.objects.filter(
            status="Запущена"
        ).count()
        unique_clients_count = Mailing.objects.values("recipients").distinct().count()
        context_data["unique_clients_count"] = unique_clients_count
        return context_data



class MailingListView(ListView):
    model = Mailing
    template_name = "emailings/mailings_list.html"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "emailings/mailings_form.html"
    success_url = reverse_lazy('emailings:mailings_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "emailings/mailings_form.html"
    success_url = reverse_lazy('emailings:mailings_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'emailings/mailings_detail.html'


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'emailings/mailings_confirm_delete.html'
    success_url = reverse_lazy('emailings:mailings_list')

