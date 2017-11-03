from utils.wrappers import *
from .models import  *
import re
from django.conf import settings
from django.core.mail import  send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def check_register_params(request):
    user_name =  post(request,'user_name')
    user_pass1 = post(request,'user_pass1')
    user_pass2 = post(request,'user_pass2')
    user_mail = post(request,'user_mail')

    flag = True
    if not (5 <= len(user_name) <= 20):
        flag = False
        # print('user_name--->',flag)
        add_info_message(request,'user_name','您输入用户名的长度不够')

    if not( 8<=len(user_pass1) <=20):
        flag = False
        # print('user_pass1--->', flag)
        add_info_message(request,'user_pass','您输入密码长度不够')

    if user_pass1 != user_pass2 :
        flag = False
        # print('user_pass2--->', flag)
        add_info_message(request,'user_pass','您输入的密码长度不够')

    if not re.match('^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',user_mail):
        flag = False
        # print('user_mail--->', flag)
        add_info_message(request,'user_mail','您输入的邮箱格式不对')


    if User.objects.get_userinfo_byname(user_name):
        flag = False
        # print('userinfobyname--->', )
        add_info_message(request,'user_name','用户名已经存在')

    print('flag result-->',flag)
    return  flag


def check_login_params(request):
    #获取登陆表单的用户名和密码
    # user_name = request.POST.get('user_name')
    user_name = post(request,'user_name')
    # user_pass = request.POST.get('user_pass')
    user_pass = post(request,'user_pass')
    # print('user_name-----+++++>',user_name)
    # print('user_pass---+++++>',user_pass)

    if not (5 <= len(user_name) <=20):
        return False
    if not(8 <= len(user_pass) <=20):
        return  False

    #数据库查询用户输入的用户名是否有对应的信息
    user = User.objects.get_userinfo_byname(user_name)
    print('user is ---->',user)
    if not user:
        return  False
    #加密是不可逆的，需要对用户的数据进行加密之后在和数据库的密码进行比较
    if user.user_pass != passwd_jiami(user_pass):
        return False
    #如果用户的user_active状态不是1说明没有激活,没有激活就不让登陆
    if user.user_active != 1:
        return False

    return  True


#保持用户登陆状态
def keep_user_online(request):
    #能执行到这说明用户名是合法的
    user_name = post(request,'user_name')
    user = User.objects.get_userinfo_byname(user_name)
    user_id = user.id
    set_session(request,'username',user_name)
    set_session(request,'userid',user_id)


def remember_username(request,response):
    #先去除用户是否点击了记住用户名
    user_remember = post(request,'user_remember')
    print('user_member',user_remember)
    if not user_remember:
        return
    user_name = post(request,'user_name')
    set_cookie(response,'username',user_name)


def add_menu_info(view_func):
    def inner(request,*args,**kwargs):
        menus = UserCenterMenu.objects.all()
        request.menus = menus
        return view_func(request,*args,**kwargs)
    return inner


# 用户联系方式信息校验
def check_user_address_params(request):
    #获得表单数据
    user_recv = post(request,'user_recv')
    user_address = post(request,'user_address')
    user_code = post(request,'user_code')
    user_tele = post(request,'user_tele')
    print('user recv is ',user_recv,'user addr',user_address, 'user_code is ',user_code,'user tele is ',user_tele)
    if (len(user_recv)) == 0:
        return False
    if (len(user_address)) == 0:
        return  False
    if (len(user_code)) != 6:
        return  False
    if (len(user_tele)) != 11:
        return False
    return True


#生成激活链接
def create_active_link(request):
    serializer = Serializer(settings.SECRET_KEY,3600)
    user = User.objects.get_userinfo_byname(post(request,'user_name'))
    token = serializer.dumps({'id':user.id})
    url = 'http://192.168.52.129:8000/users/active_handle/' +token.decode() +'/'
    # print('url is',url)
    print('url is',url)
    return  url


def send_active_mail(request):
    user_name = post(request,'user_name')
    user_mail = post(request,'user_mail')
    active_url = create_active_link(request)
    html_content = "尊敬的%s,欢迎您注册天天生鲜！<br> 点击链接完成激活<br> 激活地址是：<a href='%s'>点击激活</a>" %(user_name,active_url)
    send_mail(subject='天天生鲜激活邮件',
              message='',
              from_email=settings.EMAIL_HOST_USER,
              html_message=html_content,
              recipient_list=[user_mail],
              )

