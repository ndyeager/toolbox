# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacherId', models.CharField(unique=True, max_length=20)),
                ('schoolId', models.CharField(max_length=20)),
                ('fullName', models.ForeignKey(to='users.User')),
            ],
        ),
    ]
