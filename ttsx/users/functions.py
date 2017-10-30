from utils.getpost import *
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
        print('user_name--->',flag)

    if not( 8<=len(user_pass1) <=20):
        flag = False
        print('user_pass1--->', flag)
    if user_pass1 != user_pass2 :
        flag = False
        print('user_pass2--->', flag)
    if not re.match('^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',user_mail):
        flag = False
        print('user_mail--->', flag)

    if User.objects.get_userinfo_byname(user_name):
        return False
        # print('userinfobyname--->', )

    print('flag result-->',flag)
    return  flag


