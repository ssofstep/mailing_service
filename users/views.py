from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic.edit import CreateView, FormView
from django.core.mail import send_mail
import secrets
from config.settings import EMAIL_HOST_USER
from .forms import CustomUserCreationForm, PasswordRecoveryForm
from .models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('clients:home')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        user.token = token
        user.save()
        send_mail(
            subject="Добро пожаловать в наш сервис",
            message=f"Спасибо, что зарегистрировались в нашем сервисе! Подтвердите почту: {url} ",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)




class PasswordRecoveryView(FormView):
    template_name = "users/recovery_password.html"
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = CustomUser.objects.get(email=email)
        length = 15
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = get_random_string(length, alphabet)
        user.set_password(password)
        user.save()
        send_mail(
            subject="Восстановление пароля",
            message=f"Ваш новый пароль: {password}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
