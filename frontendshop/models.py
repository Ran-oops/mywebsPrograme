from django.db import models

# Create your models here.

#frontend页面实现的功能：
#1.验证guest登录网页
#2.guest可以看到动态加载出来的商品首页，商品列表页（可以分类显示），商品详情页（要实现放大镜功能）
#3.加入购物车，购物车要实现增减删查
#4.guest通过自己的主页看到所有的订单

#backend页面实现的功能：
#1.商品类型增删改查   获取父类型
#2.商品  增删改查
#3.所有订单信息 查看


class PGoodsType(models.Model):
    name=models.CharField(max_length=32)

class CGoodsType(models.Model):
    name=models.CharField(max_length=32)
    pgoodstype=models.ForeignKey('PGoodsType')

class GoodsInfo(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=7, decimal_places=2)  #一共7位，保留两位小数
    num =models.IntegerField()
    storename=models.CharField(max_length=50)
    description=models.TextField()
    picname=models.CharField(max_length=255)
    state=models.IntegerField()  #0表示预售 1表示在售   2表示下架
    clicknum=models.IntegerField()
    addtime=models.DateTimeField()
    goodstype=models.ForeignKey('CGoodsType')

class GuestInfo(models.Model):
    name=models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=11)
    password=models.CharField(max_length=36)
    email=models.CharField(max_length=50)
    sex=models.IntegerField()
    address=models.CharField(max_length=255)
    guestpic=models.CharField(max_length=50)

    def to_dict(self):
        return {'guid': self.id, 'name': self.name, 'phonenumber': self.phonenumber, 'address': self.address}


#比如百褶裙  买几条
class OneTypeGoodsOrder(models.Model):
    guestinfo=models.ForeignKey('GuestInfo')
    addtime=models.DateTimeField()
    consigneename=models.CharField(max_length=32)
    consigneetel=models.CharField(max_length=11)
    consigneeaddress=models.CharField(max_length=50)
    consigneecode=models.CharField(max_length=6)
    goodsinfo=models.OneToOneField('GoodsInfo')
    goodsnum=models.IntegerField()
    orderstatus=models.IntegerField()  #0表示退货  1表示换货  2表示已完成

