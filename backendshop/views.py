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
    for onechild in parentname_obj:
        getchild=onechild.cgoodstype_set.all()
        # ChildDict[onechild.name] = getchild
    # print('childname_obj', ChildDict)

    NameDict['parentname_obj'] = parentname_obj
    NameDict['ChildDict'] = ChildDict

    return render(request,'backend/Type/index.html', NameDict)


def mybackend_typeadd(request,tid):
    # return HttpResponse('hi')
    tname=PGoodsType.objects.get(id=tid).name
    return render(request, 'backend/Type/add.html',{'tid':tid, 'tname':tname})

def mybackend_typeinsert(request):
    hname=request.POST.get('cname')
    hpgoodstype_id=request.POST.get('tid')
    CGoodsType.objects.create(pgoodstype=hname,pgoodstype_id=hpgoodstype_id)

    return redirect(reverse(request,'mybackend_typeindex'))

def mybackend_typedelete(request):
    return render(request, 'backend/Type/index.html')

def mybackend_typeedit(request):
    return render(request, 'backend/Type/edit.html')

def mybackend_typeupdate(request):
    return render(request, 'backend/Type/index.html')



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











