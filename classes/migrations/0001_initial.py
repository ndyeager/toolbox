# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_admin_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=60)),
                ('classId', models.CharField(unique=True, max_length=20)),
                ('teacher', models.ForeignKey(to='users.Teacher')),
            ],
        ),
    ]
