from django.forms import ModelForm, forms
from clients.models import Clients

class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите свою почту'})
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите своё ФИО'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите комментарий'})
