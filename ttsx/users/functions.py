from utils.wrappers import *
from .models import  *
import re


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


