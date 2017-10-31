import hashlib
from utils.wrappers import *
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def passwd_jiami(password):
    sha = hashlib.sha256()
    new_password = 'hellopython' + password
    sha.update(new_password.encode('utf-8'))
    return sha.hexdigest()


def login_permission(view_func):
    def wrapper(request,*args,**kwargs):
        if get_session(request,'username') and get_session(request,'userid'):
            return view_func(request,*args,**kwargs)
        else:
            return redirect(reverse('users:login'))
    return wrapper