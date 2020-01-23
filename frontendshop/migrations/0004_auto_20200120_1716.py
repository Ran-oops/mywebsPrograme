# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendshop', '0003_auto_20200120_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='CGoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RenameModel(
            old_name='GoodsType',
            new_name='PGoodsType',
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='goodstype',
            field=models.ForeignKey(to='frontendshop.CGoodsType'),
        ),
        migrations.AddField(
            model_name='cgoodstype',
            name='pgoodstype',
            field=models.ForeignKey(to='frontendshop.PGoodsType'),
        ),
    ]
