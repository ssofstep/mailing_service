from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from emailings.models import Mailing, MailingAttempt


@login_required
def block_mailing(request, pk):
    campaign = Mailing.objects.get(pk=pk)
    campaign.is_active = {campaign.is_active: False, not campaign.is_active: True}[True]
    campaign.save()
    return redirect(reverse("mailing:mailings_list"))


def run_emailing(request, pk):
    mailing = get_object_or_404(Mailing, id=pk)
    for recipient in mailing.recipients.all():
        try:
            mailing.status = "started"
            send_mail(
                subject=mailing.message.topic,
                message=mailing.message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=[recipient.email],
                fail_silently=False,
            )
            MailingAttempt.objects.create(
                date_attempt=timezone.now(),
                status="status_ok",
                server_response="Email отправлен",
                campaign=mailing,
            )
        except Exception as e:
            print(f"Произошла ошибка при отправке письма для {recipient.email}: {str(e)}")
            MailingAttempt.objects.create(
                date_attempt=timezone.now(),
                status="status_nok",
                server_response=str(e),
                campaign=mailing,
            )
    if mailing.end_sending and mailing.end_sending <= timezone.now():
        mailing.status = "completed"
    mailing.save()
    return redirect("emailings:mailings_list")