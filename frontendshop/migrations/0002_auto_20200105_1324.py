# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='every_order',
            name='goods_to_peoplephone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='guest_info',
            name='phonenumber',
            field=models.CharField(max_length=11),
        ),
    ]
