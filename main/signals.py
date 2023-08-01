from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

from .models import UserResponse, Post


@receiver(post_save, sender=UserResponse)
def response_send(sender, instance, created, **kwargs):
    mail = instance.post.author.email

    subject = 'Новый отклик к твоему объявлению'

    text_content = (
        f'Автор: {instance.author}\n'
        f'Текст: {instance.text}\n\n'
    )
    html_content = (
        f'Автор: {instance.author}<br>'
        f'Текст: {instance.text}<br><br>'
    )
    msg = EmailMultiAlternatives(subject, text_content, None, [mail])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@receiver(post_save, sender=UserResponse)
def response_change(sender, instance, created, **kwargs):
    if instance.status == True:
        mail = instance.author.email

        subject = 'Отклик был принят'

        text_content = (
            'Отклик принят'
        )
        html_content = (
            'Отклик принят'
        )
        msg = EmailMultiAlternatives(subject, text_content, None, [mail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()