from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    avatar = models.ImageField(default='ava/avadefault.png', upload_to='ava/', verbose_name='Avatar', blank=True)
    online = models.BooleanField(default=False, verbose_name='Online/offline')

    def __str__(self):
        return self.user.username


class Chatroom(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Chat name')
    dtcreate = models.DateTimeField(auto_now_add=True, verbose_name='Datetime chat')
    owner = models.ForeignKey(Member, related_name='memberowner', on_delete=models.CASCADE, verbose_name='User-creater')
    guests = models.ManyToManyField(Member, related_name='memberguest', blank=True, verbose_name='Members of chat')

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.CharField(max_length=1024, verbose_name='Message text')
    dtcreate = models.DateTimeField(auto_now_add=True, verbose_name='Datetime message')
    author = models.ForeignKey(Member, related_name='memberauthor', on_delete=models.CASCADE,
                               verbose_name='Author message')
    room = models.ForeignKey(Chatroom, on_delete=models.CASCADE, verbose_name='In chat')

    def __str__(self):
        return self.text