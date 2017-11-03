from django.contrib import admin
from .models import *

# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
	list_display =['id','goods_name','goods_price','goods_desc']
	list_per_page =  10
admin.site.register(GoodsInfo,GoodsInfoAdmin)
