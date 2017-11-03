from django.test import TestCase
from .models import *
from django.core.urlresolvers import reverse

menu_list = [
    {'menu_name':'个人信息','menu_link':'/users/user_center','menu_flag':'info'},
    {'menu_name': '全部订单', 'menu_link': '/users/user_order/', 'menu_flag': 'order'},
    {'menu_name': '收货地址', 'menu_link': '/users/user_site/', 'menu_flag': 'site'},
]

for menu in menu_list:
    #创建模型
    ucm = UserCenterMenu()
    ucm.menu_name = menu['menu_name']
    ucm.menu_link = menu['menu_link']
    ucm.menu_flag = menu['menu_flag']
    #插入数据
    ucm.save()