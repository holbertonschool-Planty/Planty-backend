# Generated by Django 4.2.7 on 2023-11-17 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_userphoneevent_user_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userphoneevent',
            name='user_phone',
        ),
    ]
