# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_admin_student'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.ForeignKey(to='classes.Class')),
                ('student', models.ForeignKey(to='users.Student')),
            ],
        ),
    ]
