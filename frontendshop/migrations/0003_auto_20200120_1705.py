# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendshop', '0002_auto_20200105_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('num', models.IntegerField()),
                ('storename', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('picname', models.CharField(max_length=255)),
                ('state', models.IntegerField()),
                ('clicknum', models.IntegerField()),
                ('addtime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GuestInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=36)),
                ('email', models.CharField(max_length=50)),
                ('sex', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('guestpic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OneTypeGoodsOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('addtime', models.DateTimeField()),
                ('consigneename', models.CharField(max_length=32)),
                ('consigneetel', models.CharField(max_length=11)),
                ('consigneeaddress', models.CharField(max_length=50)),
                ('consigneecode', models.CharField(max_length=6)),
                ('goodsnum', models.IntegerField()),
                ('orderstatus', models.IntegerField()),
                ('goodsinfo', models.OneToOneField(to='frontendshop.GoodsInfo')),
                ('guestinfo', models.ForeignKey(to='frontendshop.GuestInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='EVERY_ORDER',
        ),
        migrations.DeleteModel(
            name='GET_GOODS_ADDRESS',
        ),
        migrations.DeleteModel(
            name='GOODS_INFO',
        ),
        migrations.DeleteModel(
            name='GUEST_INFO',
        ),
        migrations.DeleteModel(
            name='ORDER_DETAIL',
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='goodstype',
            field=models.ForeignKey(to='frontendshop.GoodsType'),
        ),
    ]
