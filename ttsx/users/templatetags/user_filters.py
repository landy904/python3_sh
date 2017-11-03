from django.template import Library
from users.models import *

register = Library()

#自定义过滤器
@register.filter
def get_menu_list(flag):
    menus = UserCenterMenu.objects.all()
    menu_list = list()

    for menu in menus:
        info = dict()
        info['menu_name'] = menu.menu_name
        info['menu_link'] = menu.menu_link
        if menu.menu_flag == flag:
            info['menu_css'] = 'active'
        else:
            info['menu_css'] = ''
        menu_list.append(info)

    return menu_list