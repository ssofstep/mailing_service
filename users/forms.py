from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField, ImageField

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            elif isinstance(fild, ImageField):
                fild.widget.attrs["class"] = "form-control-file"
            else:
                fild.widget.attrs["class"] = "form-control"


class PasswordRecoveryForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label="Укажите почту-email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Такого почты не существует")
        return email
