from django.forms import ModelForm, forms
from emailings.models import Message, Mailing


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['theme'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите тему письма'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите текст письма'})


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)

        self.fields['start_datetime'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату и время первой отправки'})
        self.fields['end_datetime'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату и время окончания отправки'})
        self.fields['status'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите статус'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите сообщение'})
        self.fields['recipients'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите получателей'})
