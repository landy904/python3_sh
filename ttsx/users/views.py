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
    print('res-->',check_register_params(request))
    if check_register_params(request):
        User.objects.register_userinfo_save(request)
        return redirect(reverse('users:login'))
    else:
        return redirect(reverse('users:register'))


# def check_username_exist(request):
#     #获取用户名,表单里面的name属性username
#     username = get(request,'username')
#     print('username is --->',username)
#     #用户名存在
#     if User.objects.get_userinfo_byname(username):
#         return  JsonResponse({'ret':1})
#     #用户名不存在
#     else:
#         return  JsonResponse({'ret':0})

# 检查用户名是否存在
def check_username_exist(request):

    # 获取用户名
    username = get(request, 'username')

    # 检查用户名是否存在
    if User.objects.get_userinfo_by_name(username):
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({'ret': 0})