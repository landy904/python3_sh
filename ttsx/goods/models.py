from db.BaseModel import *
from tinymce.models import HTMLField
from django.db import models


class GoodsCategory(BaseModel):
    goods_name = models.CharField(max_length=50)
    goods_css = models.CharField(max_length=20)
    goods_image = models.ImageField()

class GoodsInfo(BaseModel):
    goods_name = models.CharField(max_length=50)
    goods_price = models.DecimalField(max_digits=10,decimal_places=2)
    goods_short = models.CharField(max_length=100)
    goods_desc = HTMLField()
    goods_unit = models.CharField(max_length=30)
    goods_status = models.BooleanField(default=True)
    goods_sale = models.IntegerField()
    goods_visit = models.IntegerField()
    goods_img = models.ImageField()
    goods_cag = models.ForeignKey(GoodsCategory)

#商品图片
class GoodsImages(BaseModel):
    #商品路径
    img_url = models.CharField(max_length=50)
    #所属商品
    img_goods = models.ForeignKey(GoodsInfo)


class ScrollAdv(BaseModel):
    ad_name = models.CharField(max_length=30)
    ad_link = models.CharField(max_length=100)
    ad_image = models.ImageField()
    ad_index = models.SmallIntegerField()


class ActivityAdv(BaseModel):
    ac_name = models.CharField(max_length=30)
    ac_link = models.CharField(max_length=100)
    ac_image = models.ImageField()
    ac_index = models.SmallIntegerField()


