from django.shortcuts import render,HttpResponse
from .models import *
from utils.wrappers import *

# Create your views here.
def index(request):
    #最新添加的四个商品
    cags = GoodsCategory.objects.all()
    for cag in cags:
        cag.new = cag.goodsinfo_set.all().order_by('-id')[:4]
        cag.hot = cag.goodsinfo_set.all().order_by('-goods_visit')[:3]
    scradv = ScrollAdv.objects.all().order_by('ad_index')
    acvadv = ActivityAdv.objects.all().order_by('ac_index')

    return render(request,'goods/index.html',locals())

def detail(request):
    #通过商品id查询商品
    # 获取的id url地址上的id的值
    goods = GoodsInfo.objects.get(id = get(request,'id'))
    goods_new = GoodsInfo.objects.all().order_by('-id')[:2]
    return render(request,'goods/detail.html',locals())