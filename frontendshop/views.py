from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from frontendshop.models import OneTypeGoodsOrder, GoodsInfo, CGoodsType, PGoodsType, GuestInfo
# Create your views here.

#homepage
def index(request):
    return render(request,'frontend/index.html')

def login(request):
    return render(request, 'frontend/login.html')


def dologin(request):
    userphone=request.POST['usernum']
    userpassword=request.POST['password']
    certificateCode=request.POST['cCode']
    user=GuestInfo.objects.get(phonenumber=userphone)
    print(userphone)
    print(userpassword)
    print('certificateCode from html:',certificateCode)

    # import hashlib
    # m=hashlib.md5()
    # print(type(user.password))
    # m.update(bytes('123456', encoding="utf8"))
    # print("hexdigest:", m.hexdigest())
    # print("userpassword:", user.password)
    # if user.password==m.hexdigest():
    if certificateCode == request.session['certificateCode']:
        if user.password==userpassword:
            request.session['vipuser'] = user.to_dict()
            # print('this is vipuser=================', request.session['vipuser'])
            return redirect(reverse('index'))
        else:
            return HttpResponse('ERROR')
    else:
        return HttpResponse('certificate is wrong!')
def draw_certificate(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    bgcolor = (random.randrange(20,100), random.randrange(20,100), 255)
    width = 100
    height = 25
    #create picture object
    im = Image.new('RGB',(width,height), bgcolor)

    print('this is im:',im)
    #create pen object
    draw_pen = ImageDraw.Draw(im)
    #call point() function of Draw_pen to draw some point
    for i in range(0,100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0,255),255, random.randrange(0,255))
        draw_pen.point(xy, fill = fill)
    #定义验证码的备选值
    str1 = 'ABCDEFGHI1234JKLMNOPQRS890TUVWXYZ567'
    rand_str = ''
    for i in range(0,4):
        rand_str += str1[random.randrange(0, len(str1))]
        # print('this is rand_str:',rand_str)

    #create font object
    font = ImageFont.load_default().font

    fontcolor = (255, random.randrange(0,255), random.randrange(0,255))

    #to draw four letters
    draw_pen.text((10,2),rand_str[0],font=font,fill=fontcolor)
    draw_pen.text((35,2),rand_str[1],font=font,fill=fontcolor)
    draw_pen.text((60,2),rand_str[2],font=font,fill=fontcolor)
    draw_pen.text((85,2),rand_str[3],font=font,fill=fontcolor)

    del draw_pen
    request.session['certificateCode']=rand_str
    # print('rand_str:', rand_str)
    print('restored certificate:', request.session['certificateCode'])

    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def logout(request):
	del request.session['vipuser']
    # return HttpResponse('HELLO')
	return redirect(reverse('index'))



#goods_list page

def list(request):
    goodsList = {}
    goods_info = GoodsInfo.objects.all()
    # <class 'django.db.models.query.QuerySet'> 是queryset类型数据
    # print('this is goods_info:==============',goods_info,type(goods_info))
    for item in goods_info:
        print(item.picname)

    goodsList['context']=goods_info

    return render(request, 'frontend/list.html', goodsList)
	

#user detail information index page
def vipusers(request):
	return HttpResponse('this is me')


#user's shopping-cart page
def shoppingCart(request):
	return HttpResponse('my shopping-cart')