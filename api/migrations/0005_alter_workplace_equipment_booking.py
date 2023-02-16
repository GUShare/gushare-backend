# Generated by Django 4.1.7 on 2023-02-16 17:11

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_workplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workplace',
            name='equipment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('1', 'Phone'), ('2', 'Dual Screen'), ('3', 'Fax'), ('4', 'USB-C Docking-station'), ('5', 'Electric adjustable desk'), ('6', 'Printer'), ('7', 'Telephone')], max_length=3), size=None),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('started', models.DateTimeField()),
                ('stopped', models.DateTimeField()),
                ('email_others', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('confirmed_at', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(max_length=500)),
                ('workplace', models.ManyToManyField(to='api.workplace')),
            ],
        ),
    ]
