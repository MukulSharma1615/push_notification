from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class MobileDevice(models.Model):
    participant = models.OneToOneField(User, related_name='device', on_delete=models.CASCADE, null = True)
    platform = models.CharField(max_length=20, null = True, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    token = models.TextField(null = True)


class MobileNotification(models.Model):
    recipient = models.ForeignKey(User, related_name='user_device_notifications', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField(null = True)
    status = models.CharField(max_length=10, default='unread', null = True)


class InAppMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, null = True)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, null = True)
    content = models.CharField(max_length=512, null = True)