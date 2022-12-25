# Generated by Django 4.1.4 on 2022-12-21 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='memberguest', to='chatback.member', verbose_name='Members of chat'),
        ),
        migrations.AlterField(
            model_name='member',
            name='online',
            field=models.BooleanField(default=False, verbose_name='Online/offline'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]