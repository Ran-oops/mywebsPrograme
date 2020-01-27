from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from frontendshop.models import OneTypeGoodsOrder, GoodsInfo, CGoodsType, PGoodsType, GuestInfo
# Create your views here.
def backendindex(request):
    # return HttpResponse('Hi, backendpage!')
    return render(request,'backend/index.html')


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
    return HttpResponse('hi, parentTypeinsert')

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


#编辑子类别
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
    # na=request.POST['充电器']
    # print('-----thisisname：',na)
    # # return render(request, 'backend/Type/index.html')
    return HttpResponse('Hi, mybackend_typeupdate!')



#商品信息===================================================================
def mybackend_goodsindex(request):
    return HttpResponse('Hi, mybackend_goodsindex!')

def mybackend_goodsadd(request):
    return HttpResponse('Hi, mybackend_goodsadd!')

def mybackend_goodsinsert(request):
    return HttpResponse('Hi, mybackend_goodsinsert!')

def mybackend_goodsdelete(request):
    return HttpResponse('Hi, mybackend_goodsdelete!')


def mybackend_goodsedit(request):
    return HttpResponse('Hi, mybackend_goodsedit!')

def mybackend_goodsupdate(request):
    return HttpResponse('Hi, mybackend_goodsupdate!')


#查看订单
def mybackend_neworders(request):
    return HttpResponse('Hi, mybackend_neworders!')

def mybackend_historyorders(request):
    return HttpResponse('Hi, mybackend_historyorders!')











