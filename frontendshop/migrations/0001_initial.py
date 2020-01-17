# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EVERY_ORDER',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('guestid', models.IntegerField()),
                ('goods_num', models.IntegerField()),
                ('goods_type', models.CharField(max_length=30)),
                ('goods_id', models.IntegerField()),
                ('goods_descr', models.TextField()),
                ('goos_title', models.CharField(max_length=30)),
                ('goods_to_peopleid', models.IntegerField()),
                ('goods_to_peoplename', models.CharField(max_length=20)),
                ('goods_to_peoplephone', models.CharField(max_length=12)),
                ('goods_to_peoplecode', models.CharField(max_length=7)),
                ('total_price', models.FloatField()),
                ('order_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GET_GOODS_ADDRESS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('guestid', models.IntegerField()),
                ('orderid', models.IntegerField()),
                ('addresseeid', models.IntegerField()),
                ('province_id', models.IntegerField()),
                ('municipality_id', models.IntegerField()),
                ('county_id', models.IntegerField()),
                ('detaiaddress', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GOODS_INFO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goid', models.IntegerField()),
                ('typeid', models.IntegerField()),
                ('goods_title', models.CharField(max_length=30)),
                ('goods_desc', models.TextField()),
                ('goods_picname', models.CharField(max_length=30)),
                ('goods_store_num', models.IntegerField()),
                ('click_num', models.IntegerField()),
                ('goods_price', models.FloatField()),
                ('state', models.IntegerField(default=1)),
                ('merchant', models.CharField(max_length=50)),
                ('addtime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GUEST_INFO',
            fields=[
                ('guid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=36)),
                ('email', models.CharField(max_length=50)),
                ('sex', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ORDER_DETAIL',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False)),
                ('orderid', models.IntegerField()),
                ('goodsid', models.IntegerField()),
                ('goods_num', models.IntegerField()),
                ('samegoods_totalprice', models.FloatField()),
                ('allgoods_totalprice', models.FloatField()),
            ],
        ),
    ]
