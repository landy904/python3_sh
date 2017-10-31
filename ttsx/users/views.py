from django.shortcuts import render,HttpResponse,redirect
from .functions import  *
from django.core.urlresolvers import reverse
from .models import  *
from utils.wrappers import *
from django.http import  JsonResponse

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
def user_center(request):
    return render(request,'users/user_center_info.html',locals())


def logout(request):
    del_session(request)
    return redirect(reverse('users:login'))
