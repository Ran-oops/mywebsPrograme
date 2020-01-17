from django.db import models

# Create your models here.

class GUEST_INFO(models.Model):
    guid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=11)
    password=models.CharField(max_length=36)
    email=models.CharField(max_length=50)
    sex=models.IntegerField()
    address=models.CharField(max_length=255)

    def to_dict(self):
        return {'guid': self.guid, 'name': self.name, 'phonenumber': self.phonenumber, 'address': self.address}


class GOODS_INFO(models.Model):
    goid=models.IntegerField()
    typeid=models.IntegerField()
    goods_title=models.CharField(max_length=30)
    goods_desc=models.TextField()
    goods_picname=models.CharField(max_length=30)
    goods_store_num=models.IntegerField()
    click_num=models.IntegerField()
    goods_price=models.FloatField()
    state=models.IntegerField(default=1)
    merchant=models.CharField(max_length=50)
    addtime=models.DateField()



class EVERY_ORDER(models.Model):
    oid=models.AutoField(primary_key=True)
    guestid=models.IntegerField()
    goods_num=models.IntegerField()
    goods_type=models.CharField(max_length=30)
    goods_id=models.IntegerField()
    goods_descr=models.TextField()
    goos_title=models.CharField(max_length=30)
    goods_to_peopleid=models.IntegerField()
    goods_to_peoplename=models.CharField(max_length=20)
    goods_to_peoplephone=models.CharField(max_length=11)
    goods_to_peoplecode=models.CharField(max_length=7)
    total_price=models.FloatField()
    order_status=models.IntegerField()

class ORDER_DETAIL(models.Model):
    did=models.IntegerField(primary_key=True)
    orderid=models.IntegerField()
    goodsid=models.IntegerField()
    goods_num=models.IntegerField()
    samegoods_totalprice=models.FloatField()
    allgoods_totalprice=models.FloatField()


class GET_GOODS_ADDRESS(models.Model):
    guestid=models.IntegerField()
    orderid=models.IntegerField()
    addresseeid=models.IntegerField()
    province_id=models.IntegerField()
    municipality_id=models.IntegerField()
    county_id=models.IntegerField()
    detaiaddress=models.CharField(max_length=50)




