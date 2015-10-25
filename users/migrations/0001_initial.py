# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('user_type', models.CharField(default=b'Teacher', max_length=20, choices=[(b'Administrator', b'Administrator'), (b'Teacher', b'Teacher'), (b'Student', b'Student')])),
            ],
        ),
    ]
