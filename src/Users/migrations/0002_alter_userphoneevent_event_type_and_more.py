# Generated by Django 4.2.7 on 2023-11-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoneevent',
            name='event_type',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='userphoneevent',
            name='message',
            field=models.CharField(),
        ),
    ]