from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from books.models import User


@receiver(post_save, sender=User)
def notify_admin_with_moderator_create(sender, instance, created, **kwargs):
    if created and instance.is_staff and instance.role == "MODERATOR":
        subject = "New Moderator"
        sender = "no-reply.160924_ptm@gmail.com"
        recipient = 'admin.mail@gmail.com'

        context = {
            "email": instance.email,
            "username": instance.username
        }

        text_context = render_to_string(
            template_name='new_moderator.txt',
            context=context
        )

        html_context = render_to_string(
            template_name='new_moderator.html',
            context=context
        )

        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_context,
            from_email=sender,
            to=[recipient],
            headers={'List-Unsubscribe': '<mailto:unsub@example.com>'}
        )

        msg.attach_alternative(
            html_context,
            'text/html'
        )

        msg.send()
