from django.forms import ModelForm, forms
from emailings.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['theme'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите тему письма'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите текст письма'})
