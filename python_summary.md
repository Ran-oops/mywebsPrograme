## 关于Django ORM 操作
### 增加数据
```
ob=Users() #实例化一个对象
ob.name = 'zhangsan'
ob.id = 3
ob.publish_id =3
ob.save()
```


### 查看数据
```
# -*- coding: utf-8 -*-

#获取数据的多种操作

 

from django.http import HttpResponse

 

from TestModel.models import Test

 

# 数据库操作

def testdb(request):

    # 初始化

    response = ""

    response1 = ""

    

    

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM

    list = Test.objects.all()

        

    # filter相当于SQL中的WHERE，可设置条件过滤结果

    response2 = Test.objects.filter(id=1) 

    

    # 获取单个对象

    response3 = Test.objects.get(id=1) 

    response4 = Test.objects.first() 

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;

    Test.objects.order_by('name')[0:2]

    

    #数据排序

    Test.objects.order_by("id")

    

    # 上面的方法可以连锁使用

    Test.objects.filter(name="runoob").order_by("id")

    

    # 输出所有数据

    for var in list:

        response1 += var.name + " "

    response = response1

    return HttpResponse("<p>" + response + "</p>")
```

### 更改数据 更改数据用save()或者update()

```

# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test

 

# 数据库操作

def testdb(request):

    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE

    test1 = Test.objects.get(id=1)

    test1.name = 'Google'

    test1.save()

    

    # 另外一种方式

    #Test.objects.filter(id=1).update(name='Google')

    

    # 修改所有的列

    # Test.objects.all().update(name='Google')

    

    return HttpResponse("<p>修改成功</p>")
```

### 删除数据 删除数据delete()
```

# -*- coding: utf-8 -*-

 

from django.http import HttpResponse

 

from TestModel.models import Test

 

# 数据库操作

def testdb(request):

    # 删除id=1的数据

    test1 = Test.objects.get(id=1)

    test1.delete()

    

    # 另外一种方式

    # Test.objects.filter(id=1).delete()

    

    # 删除所有数据

    # Test.objects.all().delete()

    

    return HttpResponse("<p>删除成功</p>")
```

转自：[原文地址](https://blog.csdn.net/zoukai1587/article/details/88776214)


delete()

.update()  #只适用于filter的情况   filter的结果是0个或多个对象组成的列表  get只有一个对象
save()

get()
filter()



[](https://www.cnblogs.com/morgana/p/8492895.html)

