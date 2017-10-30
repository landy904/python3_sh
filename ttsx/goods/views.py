from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('商品首页')