# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_classroster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(related_name='classes', to='users.Teacher'),
        ),
    ]
