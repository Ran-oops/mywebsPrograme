# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendshop', '0002_auto_20200120_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cgoodstype',
            name='pgoodstype',
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='goodstype',
        ),
        migrations.RemoveField(
            model_name='onetypegoodsorder',
            name='goodsinfo',
        ),
        migrations.RemoveField(
            model_name='onetypegoodsorder',
            name='guestinfo',
        ),
        migrations.DeleteModel(
            name='CGoodsType',
        ),
        migrations.DeleteModel(
            name='GoodsInfo',
        ),
        migrations.DeleteModel(
            name='GuestInfo',
        ),
        migrations.DeleteModel(
            name='OneTypeGoodsOrder',
        ),
        migrations.DeleteModel(
            name='PGoodsType',
        ),
    ]
