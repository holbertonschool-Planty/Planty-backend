# Generated by Django 4.2.6 on 2023-11-04 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Devices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_planty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('plant_name', models.CharField()),
                ('image_url', models.URLField(blank=True)),
                ('location', models.CharField(default='room')),
                ('color_card', models.CharField(default='#38CE61', max_length=7)),
                ('planty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.planty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
