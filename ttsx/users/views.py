from django.shortcuts import render,HttpResponse,redirect
from .functions import  *
from django.core.urlresolvers import reverse
from .models import  *
from utils.wrappers import *
from django.http import  JsonResponse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings

# Create your views here.
def index(request):
    return HttpResponse('用户中心')


def login(request):
    return render(request,'users/login.html')


def register(request):
    message = get_info_messge(request)
    return render(request,'users/register.html',locals())


def register_handle(request):
    # print('res-->',check_register_params(request))
    if check_register_params(request):
        User.objects.register_userinfo_save(request)
        #调用发送邮件的函数
        send_active_mail(request)
        return redirect(reverse('users:login'))
    else:
        return redirect(reverse('users:register'))


def check_username_exist(request):
    #获取用户名,表单里面的name属性username
    username = get(request,'username')
    print('username is --->',username)
    #用户名存在
    if User.objects.get_userinfo_byname(username):
        return  JsonResponse({'ret':1})
    #用户名不存在
    else:
        return  JsonResponse({'ret':0})

def login_handle(request):
    #对登陆页面的输入数据进行校验
    # print('检查登陆参数--->', check_login_params(request))
    if check_login_params(request):
        #保持用户登陆状态
        keep_user_online(request)
        #保持用户名
        response = redirect(reverse('users:user_center'))
        remember_username(request,response)
        return  response
    #数据校验不成功重新跳转到登陆页面
    else:
        return redirect(reverse('users:login'))


@login_permission
@add_menu_info
def user_center(request):
    # menus = UserCenterMenu.objects.all()
    user = User.objects.get_userinfo_byname(get_session(request,'username'))
    return render(request,'users/user_center_info.html',locals())


@login_permission
@add_menu_info
def user_order(request):
    # menus = UserCenterMenu.objects.all()
    return render(request,'users/user_center_order.html',locals())


@login_permission
@add_menu_info
def user_site(request):
    # menus = UserCenterMenu.objects.all()
    user = User.objects.get_userinfo_byname(get_session(request, 'username'))
    return render(request,'users/user_center_site.html',locals())


def logout(request):
    del_session(request)
    return redirect(reverse('users:login'))


def update_address(request):
    #校验参数
    print('check user address params',check_user_address_params(request))
    if check_user_address_params(request):

        #如果通过，就更新入库
        # print('入库之前')
        User.objects.update_user_address(request)
        # print('入库之后')

    return redirect(reverse('users:user_site'))


def active_handle(request,token):
    # print('test bug test bug ')
    serializer = Serializer(settings.SECRET_KEY,3600)
    try:
        # print('1111111111111111111111111111111111111111111111111')
        user_id = serializer.loads(token).get("id")
        # 获得激活链接中的用户ID
        print('user_id is',user_id)
        user = User.objects.get(id = user_id)
        # print('user id and user',user_id,user)
        user.user_active = True
        # print('user active is ',user.user_active)
        user.save()
        # print('激活成功')
        # return HttpResponse('用户激活成功')
        # if user.user_active  == True:
        #成功激活跳转到登陆页面
        return redirect(reverse('users:login'))
    except:
        return HttpResponse('激活链接已经过期')


def  my_send_mail(request):

    return HttpResponse('发送邮件成功')