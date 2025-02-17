from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from emailings.forms import MessageForm
from emailings.models import Message


class MessageListView(ListView):
    model = Message
    template_name = 'emailings/emailings_list.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'emailings/emailings_form.html'
    success_url = reverse_lazy('emailings:emailings_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'emailings/emailings_form.html'
    success_url = reverse_lazy('emailings:emailings_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'emailings/emailings_detail.html'


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'emailings/emailings_confirm_delete.html'
    success_url = reverse_lazy('emailings:emailings_list')


class HomeView(TemplateView):
    template_name = 'emailings/home.html'
