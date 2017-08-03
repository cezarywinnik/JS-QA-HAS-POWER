# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 14:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_invitations', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_invitations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]