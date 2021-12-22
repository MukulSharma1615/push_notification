from django.dispatch import receiver
from .models import *
from .tasks_celery import *
from django.db.models.signals import post_save

@receiver(post_save, sender=InAppMessage)
def send_new_message_notification(sender, **kwargs):
    message = kwargs['instance']
    print('message:- ',message)
    print(message.sender.id)
    print(message.recipient.id)
    send_new_message_push_notification.delay(sender_id=message.sender.id,
                                             recipient_id=message.recipient.id,
                                             content=message.content)