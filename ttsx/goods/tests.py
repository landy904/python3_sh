from django.test import TestCase
from .models import *
import random

categories = [
    {'goods_name': '新鲜水果', 'goods_css': 'fruit', 'goods_image': 'images/banner01.jpg'},
    {'goods_name': '海鲜水产', 'goods_css': 'seafood', 'goods_image': 'images/banner02.jpg'},
    {'goods_name': '猪牛羊肉', 'goods_css': 'meet', 'goods_image': 'images/banner03.jpg'},
    {'goods_name': '禽类蛋品', 'goods_css': 'egg', 'goods_image': 'images/banner04.jpg'},
    {'goods_name': '新鲜蔬菜', 'goods_css': 'vegetables', 'goods_image': 'images/banner05.jpg'},
    {'goods_name': '速冻食品', 'goods_css': 'ice', 'goods_image': 'images/banner06.jpg'},
]

for cag in categories:
    c = GoodsCategory()
    c.goods_name = cag['goods_name']
    c.goods_css = cag['goods_css']
    c.goods_image = cag['goods_image']
    c.save()

units = ['1个', '1头', '1坨', '1吨', '1克', '500克', '2箱', '1车', '10条']
with open('/data/server/ttsx_three_py3/python3_sh/ttsx/data.txt','r') as f:
    for name in f:
        g = GoodsInfo()
        print('name is:',name[:-1])
        g.goods_name = name[:-1]
        g.goods_price = random.randint(100,999)
        g.goods_cag_id = random.randint(1,6)
        g.goods_desc = '商品非常好，价格便宜，童叟无欺哦!'
        g.goods_short = '商品真的是非常好啊，日销量过万，在不买就没了!'
        g.goods_img = 'goods/' +str(random.randint(1,18)) + '.jpg'
        g.goods_sale = 0
        g.goods_unit = units[random.randint(0,len(units) -1)]
        g.goods_visit = 0
        #print('goods_time',g.goods_time,g.goods_price,g.goods_desc,g.goods_short,g.goods_img)
        g.save()


for index in range(1,5):
    sa = ScrollAdv()
    sa.ad_name = '首页轮播广告'
    sa.ad_image = 'images/slide0' +str(index) +'.jpg'
    sa.ad_index ='#'
    sa.ad_index = index
    sa.save()


for index in range(1,3):
    aa = ActivityAdv()
    aa.ad_name = '劲爆广告'
    aa.ac_image = 'images/adv0' + str(index) +'.jpg'
    aa.ac_link ='#'
    aa.ac_index = index
    aa.save()
