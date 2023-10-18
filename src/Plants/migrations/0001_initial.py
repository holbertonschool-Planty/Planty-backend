# Generated by Django 4.2.6 on 2023-10-18 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants_info',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('scientific_name', models.CharField(max_length=100, unique=True)),
                ('station', models.CharField(max_length=40)),
                ('temperature', models.PositiveSmallIntegerField()),
                ('light', models.PositiveSmallIntegerField()),
                ('watering', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
