import datetime
import time
import os
from PIL import Image
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from frontendshop.models import OneTypeGoodsOrder, GoodsInfo, CGoodsType, PGoodsType, GuestInfo
# Create your views here.
def backendindex(request):
    # return HttpResponse('Hi, backendpage!')
    return render(request,'backend/index(1).html')


#种类
def mybackend_typeindex(request):
    NameDict = {}
    ChildDict = {}

    parentname_obj = PGoodsType.objects.all()
    child_obj = CGoodsType.objects.all()
    for onechild in parentname_obj:
        getchild=onechild.cgoodstype_set.all()
        # ChildDict[onechild.name] = getchild
    # print('childname_obj', ChildDict)

    # NameDict['parentname_obj'] = parentname_obj
    # NameDict['ChildDict'] = ChildDict

    return render(request,'backend/Type/index.html', {'parent':parentname_obj, 'child': child_obj})

#增加父类别
def mybackend_ptypeadd(request):

    return render(request, 'backend/Type/padd.html')

def mybackend_ptypeinsert(request):
    pname=request.POST['pname']
    print('======================pname:',pname)
    PGoodsType.objects.create(name=pname)
    return redirect(reverse('mybackend_typeindex'))
    # return HttpResponse('hi, parentTypeinsert')

#添加子类别
def mybackend_typeadd(request,tid):
    # return HttpResponse('hi')
    tname=PGoodsType.objects.get(id=tid).name
    return render(request, 'backend/Type/add.html',{'tid':tid, 'tname':tname})

def mybackend_typeinsert(request):
    hname=request.POST.get('cname')
    hid = request.POST.get('tid')
    hid = int(hid)
    print('*************hname:',hname, type(hname))
    print('*************hpgoodstype_id:',hid, type(hid))

    CGoodsType.objects.create(name=hname, pgoodstype_id=hid)
    return redirect(reverse('mybackend_typeindex'))


    # return HttpResponse('hi,OK！')
#父类别删除
def mybackend_typedelete(request, tid):
    PGoodsType.objects.filter(id=tid).delete()
    return redirect(reverse('mybackend_typeindex'))

#编辑父类别
def mybackend_ptypeedit(request, tid):
    ptype=PGoodsType.objects.filter(id=tid).first()
    print('-------------ptype:', ptype)
    # return HttpResponse('hi,ptypeedit')
    return render(request, 'backend/Type/pedit.html', {'type':ptype})


def mybackend_ptypeupdate(request, tid):
    name=request.POST['pname']
    print('from parents edit=======:',name)
    PGoodsType.objects.filter(id=tid).update(name=name)
    # return HttpResponse('hi,ptypeupdate')
    return redirect(reverse('mybackend_typeindex'))


#编辑子类别(包含删除操作)
def mybackend_typeedit(request, tid):
    child_obj=CGoodsType.objects.filter(pgoodstype_id=tid)

    return render(request, 'backend/Type/edit.html', {'child_obj':child_obj, 'tid':tid})

def mybackend_typeupdate(request, tid):
    # c_obj=CGoodsType.objects.filter(pgoodstype_id=tid)
    # 注意这边出过错是用了filter报Queryset has no attribute cgoodstype,换成get就好了或者是filter后first()  如下：
    p_obj=PGoodsType.objects.filter(id=tid).first()
    all=p_obj.cgoodstype_set.all()
    for item in all:
        print(item.name)
        n=item.name
        i=item.pgoodstype_id
        na=request.POST[n]
        print('-----thisisname：',na)
        print('-----thisisid：',i, type(i))
        if na == '':
            CGoodsType.objects.filter(name=n).delete()
            print('hi,no')
        else:
            CGoodsType.objects.filter(name=n).update(name=na, pgoodstype_id=i)

            print('hi,yes')

    # CGoodsType.objects.filter(name='手机壳').update(name='box', pgoodstype_id=2)
    # CGoodsType.objects.filter(name='box').delete()

    return redirect(reverse('mybackend_typeindex'))
    # return HttpResponse('Hi, mybackend_typeupdate!')



#商品信息===================================================================
def mybackend_goodsindex(request):
    goods=GoodsInfo.objects.all()
    return render(request, 'backend/goods/index(1).html', {'goods':goods})
    # return HttpResponse('Hi, mybackend_goodsindex!')

def mybackend_goodsadd(request):
    types=CGoodsType.objects.all()
    return render(request, 'backend/goods/add.html',{'types':types})
    # return HttpResponse('Hi, mybackend_goodsadd!')

def mybackend_goodsinsert(request):
    print('settings', settings.STATIC_URL)
    dest='static/mybackend/img/goods/'    #注意： goods后面一定要加/， 否则会有反斜杠\\会报错
    print('dest=====:', dest)
    misfile=request.FILES.get('pic', None)
    if not misfile:
        return HttpResponse(' there is not any files')

    #判断并执行图片的上传，缩放等处理
    #split('.')是返回以.分割字段组成的列表
    #pop（）是默认弹出列表中的最后一个
    #以时间戳命名上传的这张照片
    filename = str(time.time())+"."+misfile.name.split('.').pop()
    destination = open(os.path.join(dest, filename), "wb+")
    for chunk in misfile.chunks():
        destination.write(chunk)
    destination.close()

    # filename = str(time.time())+"."+misfile.name.split('.').pop()
    # destination = open(os.path.join(settings.UPLOADFILES_DIRS, filename), "wb+")
    # for chunk in misfile.chunks():
    #     destination.write(chunk)
    # destination.close()
    #
    #执行图片缩放
    im=Image.open(dest + filename)
    #缩放到375*375
    im.thumbnail((375,375))
    #把缩放后的图像用jpeg格式保存
    im.save(dest + filename, 'jpeg')

    #缩放到220*220
    im.thumbnail((220,220))
    im.save(dest + 'm_' + filename, 'jpeg')

    #缩放到100*100
    im.thumbnail((100,100))
    im.save(dest + 's_' + filename, 'jpeg')
    picnames=filename

    titles=request.POST['goods']
    prices=request.POST['price']
    nums=request.POST['store']
    storenames=request.POST['company']
    descriptions=request.POST['descr']
    # picname=request.POST['goods']
    states=request.POST['state']
    addtimes=datetime.datetime.now()
    goodstype_ids=request.POST['typeid']
    clicknum = 0
    GoodsInfo.objects.create(title=titles, price=prices,num=nums,storename=storenames,description=descriptions,picname=picnames,state=states,addtime=addtimes,goodstype_id=goodstype_ids, clicknum=clicknum)

    # print('filename===========:',filename, type(filename))
    # return HttpResponse('Hi, mybackend_goodsinsert!')
    return redirect(reverse('mybackend_goodsindex'))

def mybackend_goodsdelete(request, tid):
    picname=GoodsInfo.objects.filter(id=tid).first().picname
    dest = 'static/mybackend/img/goods/'
    os.remove(dest + picname)
    os.remove(dest + 'm_' + picname)
    os.remove(dest + 's_' + picname)
    GoodsInfo.objects.filter(id=tid).delete()
    return redirect(reverse('mybackend_goodsindex'))


def mybackend_goodsedit(request, tid):
    print('tid...................:', tid)

    goods = GoodsInfo.objects.filter(id=tid).first()
    print('goods:', goods.clicknum)
    types = CGoodsType.objects.all()
    return render(request, 'backend/goods/edit.html', {'goods':goods,'types':types})
    # return HttpResponse('Hi, mybackend_goodsedit!')

def mybackend_goodsupdate(request, tid):
    myfile=request.FILES.get('pic', None)
    if myfile:
        oldpicname = request.POST['oldpicname']
        dest = 'static/mybackend/img/goods/'
        os.remove(dest + oldpicname)
        os.remove(dest + 'm_' + oldpicname)
        os.remove(dest + 's_' + oldpicname)

        filename=str(time.time())+"."+myfile.name.split('.').pop()
        destination=open(os.path.join(dest,filename), 'wb+')

        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()

        #执行缩放
        im=Image.open(dest + filename)
        im.thumbnail((375,375))
        im.save(dest+filename,'jpeg')

        im.thumbnail((220, 220))
        im.save(dest + 'm_' + filename, 'jpeg')

        im.thumbnail((100, 100))
        im.save(dest + 's_' + filename, 'jpeg')
        picnames=filename
    else:
        oldpicname=request.POST['oldpicname']
        picnames =oldpicname
    # clicknums=request.POST['clicknum']
    titles=request.POST['goods']
    prices=request.POST['price']
    nums=request.POST['store']
    storenames=request.POST['company']
    descriptions=request.POST['descr']
    states=request.POST['state']
    addtimes=datetime.datetime.now()
    goodstype_ids=request.POST['typeid']
    GoodsInfo.objects.filter(id=tid).update(title=titles, price=prices,num=nums,storename=storenames,description=descriptions,picname=picnames,state=states,addtime=addtimes,goodstype_id=goodstype_ids)

    return redirect(reverse('mybackend_goodsindex'))
    # return HttpResponse('Hi, mybackend_goodsupdate!')


#查看订单
def mybackend_neworders(request):
    return HttpResponse('Hi, mybackend_neworders!')

def mybackend_historyorders(request):
    return HttpResponse('Hi, mybackend_historyorders!')











