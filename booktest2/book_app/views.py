from django.shortcuts import render,redirect
from .models import *
from datetime import date
from django.http import HttpResponseRedirect
from django.http import  JsonResponse,HttpResponse
from django.conf import  settings
from django.core.mail import send_mail
from PIL import  Image,ImageDraw,ImageFont
from django.utils.six import  BytesIO
from django.core.paginator  import Paginator



# Create your views here.
def index(request):
  booklist = BookInfo.objects.all()
  #将图书列表传递到模板中，然后渲染模板
  print('生成相应对象,在执行return 给用户前，打印一句我是index')
  # raise Exception('自定义的异常')
  return render(request, 'book_app/index.html', {'Tem_booklist': booklist,"Tem_title":"图书列表"})

def detail(reqeust, bid):
    #根据图书编号对应图书
	book = BookInfo.objects.get(id=int(bid))
    #查找book图书中的所有英雄信息
	heros = book.heroinfo_set.all()
    #将图书信息传递到模板中，然后渲染模
	return render(reqeust, 'book_app/detail.html', {'book':book,'heros':heros})

def create(request):
	book = BookInfo()
	book.btitle ="流星蝴蝶剑"
	book.bpub_date = date(1996,12,23)
	book.save()
	return redirect('/')

def delete(request,id):
	book = BookInfo.books.get(pk=int(id))
	book.isDelete = True
	book.save()
	return redirect('/')


def area(request, aid):
	area = AreaInfo.objects.get(pk=int(aid))
	return render(request,'book_app/area.html',{'area':area})


def get(request):
	dict = request.GET
	a = dict.get('a')
	b = dict.get("b")
	c = dict.get('c')
	d = dict.get('d','4')
	e = dict.get('e')
	context = {'a':a,'b':b,'c':c,'d':d,'e':e}
	return render(request,'book_app/get_one.html',context)


def post_index(request):
	return render(request,'book_app/post_index.html')


def post_b(request):
    name = request.POST.get('name')
    # 指定一个获取密码的属性
    pwd = request.POST.get('pwd')
    # 指定一个获取性别的属性
    gender = request.POST.get('gender')
    # 指定一个获取爱好的属性
    hobbys = request.POST.get('hobby')
    context = {'T_name': name, 'T_pwd': pwd, 'T_gender': gender, 'T_hobbys': hobbys}
    return render(request, 'book_app/post_b.html', context)


# def redirect(request):
#     return HttpResponseRedirect("/get")


def ajax_index(request):
    return render(request,'book_app/ajax_1.html')


def json_data(request):
    booklist = BookInfo.objects.all()
    list = []
    for book in booklist:
        list.append({"name":book.btitle})
    jsondict = {"booklist":list}
    return  JsonResponse(jsondict)

def cookie_set(request):
    Response = HttpResponse("<h1>设置cookie,请查看相应包文头</h1>")
    Response.set_cookie("cookie2","ckvalue2")
    return Response

def cookie_get(request):
    if 'cookie2' in request.COOKIES:
        val = request.COOKIES['cookie2']
    else:
        val  = 'cookie 不存在'
    return HttpResponse(val)


def test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("tsta")

def get_cookie(request):
    ret = request.session.test_cookie_worked()
    if ret:
        val = "验证成功"
        request.session.delete_test_cookie()
    else:
        val ="验证失败"
    return HttpResponse(val)

def delete_cookie(request):
    Response = HttpResponse('<h1>删除cookies,请查看相应报文</h1>')
    Response.delete_cookie('cookie2')
    # return HttpResponse(Response)
    return Response


def session_test(request):
    request.session['h1'] ='hello1'
    return HttpResponse('写session ok')


def get_session(request):
    sess = request.session.get('h1')
    return HttpResponse('sess')


def session_test2(request):
    request.session['h3'] ='helloworld3'
    return HttpResponse('ok')

def del_session(request):
    del request.session['h1']
    return HttpResponse("删除session ok")

def session_read(request):
    h1 = request.session.get('h4')
    return HttpResponse(h1)

def clear_session(request):
    request.session.clear()
    return HttpResponse("clear 删除所有的健的值")



def flush_session(request):
    request.session.flush()
    return HttpResponse('清除session数据，包括健以及值')


def redis_session(request):
    request.session['u1'] = 'tudou'
    return HttpResponse('it is ok')


# def getcookie(request):
#     response = HttpResponse("读取Cookie，数据如下：<br>")
#     if request.COOKIES.has_key()
#         response.write('<h1>' + request.COOKIES['cookie1'] + '</h1>')
#     return response


def book(request):
    booklist = BookInfo.objects.all()
    # booklist = []
    context = {"Tem_booklist":booklist,"Tem_title":"图书信息"}
    return render(request,'book_app/book.html',context)


def session1(request):
    uname = request.session.get('myname','未登陆')
    context = {'uname':uname}
    print('session1')
    return render(request,'book_app/session1.html',context)


def session2(request):
    print('session2')
    return render(request,'book_app/session2.html')


def session2_handle(request):
    print('session2_handler')
    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect('/book_app/session1/')


def session3(request):
    print('session3')
    del request.session['myname']
    return redirect('/book_app/session1/')

def static_test(request):
    return render(request,'book_app/static_file_2.html')

# 定义一个接受请求的函数，返回一个模板文件
def pic_upload(request):
    return render(request,'book_app/pic_upload.html')


def pic_handle(request):
    # 从request 的FILES 请求中，获取键为pic 的值，这个pic 值是我们提交表单中定义的
    #获取上传的图片数据流
    f1=request.FILES.get('pic')
    # 定义一个服务器上的文件上传地址：media/book_app/jingtai.jpg
    fname='%s/book_app/%s'%(settings.MEDIA_ROOT,f1.name)
    # 使用with 方式打开我们刚才定义的fname 文件，格式是wb，然后定义这个对象为pic

    with open(fname,'wb') as pic:
    # 遍历网络传输过来的文件数据流，
        #chunks()方法读取网络中的文件的数据流
        for c in f1.chunks():
        #将传输时候一段一段的数据存储到我们的fname 中
            pic.write(c)
    #刚才是将网络中的文件流，写到系统的磁盘上，并没有进行数据库的记录增加
    # 定义一个实例对象
    P1 = PicTest()
    # 给数据库中添加的数据记录为：book_app/jingtai.jpg
    P1.pic = 'book_app/%s'%f1.name
    # 对数据库对象操作，最后一步是保存数据
    P1.save()
    return HttpResponse('ok')


def show_pic(request):
    pic = PicTest.objects.all()
    context ={'Tem_pic':pic}
    return render(request,'book_app/show_pic.html',context)


def editor(request):
   return render(request,'book_app/editor.html')


def show(request):
    goods = GoodsInfo.objects.all()
    context = {'goods':goods}
    return render(request,'book_app/show.html',context)


def send_mail(request):
    msg='<a href="http://www.itcast.cn/subject/pythonzly/index.shtml" target="_blank">点击激活</a>'
    send_mail('注册激活','',settings.EMAIL_FROM,
              ['553895596@qq.com'],
              html_message=msg)
    return HttpResponse('ok')


def verify_code(request):
    import  random
    bgcolor = (random.randrange(20,100),random.randrange(20,100),255)
    width = 100
    height = 25
    im = Image.new('RGB',(width,height),bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    str1 ="abcdefghljkmnopqrstuvwxyzABCDEFGHLKJLMNOPRQSTUVWXYZ0123456789"
    str2 = ""
    for i in range(0,4):
        str2 += str1[random.randrange(0,len(str1))]
    font =ImageFont.truetype('FreeMono.ttf',23)
    fontcolor =(255,random.randrange(0,255),random.randrange(0,255))
    draw.text((5,2),str2[0],font=font,fill=fontcolor)
    draw.text((25,2),str2[1],font=font,fill=fontcolor)
    draw.text((50,2),str2[2],font=font,fill=fontcolor)
    draw.text((75,2),str2[3],font=font,fill=fontcolor)
    del draw
    request.session['verifycode'] = str2
    buf = BytesIO()
    im.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')

def verify_show(request):
    return render(request,'book_app/verify_show.html')

def verify_yz(request):
    yzm = request.POST.get('yzm')
    print('1--->',yzm)
    verifycode = request.session['verifycode']
    print('2--->',verifycode)
    res = HttpResponse('NO')
    if yzm == verifycode:
        res = HttpResponse('验证通过')
    # else:
        # response = HttpResponse('输入错误')
    return res


def page_test(request,pnum):
    hero = HeroInfo.objects.all()
    danye = Paginator(hero,5)
    if pnum =='':
        pnum = 1
    page_content = danye.page(int(pnum))
    page_num = danye.page_range
    context = {'Tem_title':'人物详情页','Tem_renwu':page_content,'Tem_pnum':page_num}
    return render(request,'book_app/fenye.html',context)

def cengjixuanze(request):
    return render(request,'book_app/cengjixuanzhe.html')


def TuShu(request):
    tushu = BookInfo.objects.all()
    tushu_list = []
    for ts in tushu:
        tushu_list.append([ts.id,ts.btitle])
    tushu_dict = {'Tudic':tushu_list}
    return JsonResponse(tushu_dict)


def RenWu(request,sid):
    renwu = HeroInfo.objects.filter(hbook_id = int(sid))
    renwu_list = []
    for rw in renwu:
        renwu_list.append({'heroname':rw.hname})
    renwu_dict = {'RenWuDic':renwu_list}
    return JsonResponse(renwu_dict)


def areainfo_page(request,pindex):
    list1 = AreaInfo.objects.filter(aParent__isnull=True)
    p =Paginator(list1,10)
    if pindex =='':
        pindex = 1
    pindex = int(pindex)
    plist = p.page_range
    #list2是获取某一页的所有内容
    list2 = p.page(pindex)
    context ={'list':list2,'plist':plist,'pindex':pindex}
    return render(request,'book_app/areainfo_page.html',context)


def area1(request):
    return render(request,'book_app/area1.html')

def area2(request):
    list1 = AreaInfo.objects.filter(aParent__isnull=True)
    list2 = []
    for area in list1:
        list2.append([area.id,area.atitle])
    area_dict = {'data':list2}
    return JsonResponse(area_dict)

def area3(request,pid):
    list3 = AreaInfo.objects.filter(aParent_id=pid)
    list4 = []
    for item in list3:
        list4.append({'id':item.id,'title':item.atitle})
    return JsonResponse({'data':list4})




