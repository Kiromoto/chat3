from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(default='ava/avadefault.png', upload_to='ava/', verbose_name='Avatar', blank=True)

class Chatroom(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Message(models.Model):
    text = models.CharField(max_length=1024)
