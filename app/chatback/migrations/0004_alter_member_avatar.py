# Generated by Django 4.1.4 on 2023-01-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatback', '0003_alter_member_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, default='ava/avadefault.png', upload_to='ava/', verbose_name='Avatar'),
        ),
    ]
