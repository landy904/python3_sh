from django.shortcuts import render,HttpResponse,redirect
from .functions import  *
from django.core.urlresolvers import reverse
from .models import  *

# Create your views here.
def index(request):
    return HttpResponse('用户中心')


def login(request):
    return render(request,'users/login.html')


def register(request):
    return render(request,'users/register.html')


def register_handle(request):
    print('res-->',check_register_params(request))
    if check_register_params(request):
        User.objects.register_userinfo_save(request)
        return redirect(reverse('users:login'))
    else:
        return redirect(reverse('users:register'))