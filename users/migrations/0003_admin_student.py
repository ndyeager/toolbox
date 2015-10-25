# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schoolId', models.CharField(max_length=20)),
                ('schoolName', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=2)),
                ('fullName', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentId', models.CharField(unique=True, max_length=20)),
                ('schoolId', models.CharField(max_length=20)),
                ('fullName', models.ForeignKey(to='users.User')),
            ],
        ),
    ]
