#coding:utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class BookInfo(models.Model):
	btitle = models.CharField(max_length=20)
	bpub_date = models.DateField()#发布日期
	bread = models.IntegerField(default=0)#阅读量
	bcomment = models.IntegerField(default=0)#评论量
	isDelete = models.BooleanField(default = False) #逻辑删除
	# books = BookInfoManager()
	def __str__(self):
		return self.btitle


class HeroInfo(models.Model):
	hname = models.CharField(max_length=20)#英雄姓名
	hgender = models.BooleanField(default=True)#英雄性别
	isDelete = models.BooleanField(default=False)#逻辑删除
	hcomment = models.CharField(max_length=200)#英雄描述信息
	hbook = models.ForeignKey('BookInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中
	def __str__(self):
		return self.hname

	# def gongfu(self):
	# 	return self.hcomment
	# gongfu.admin_order_field='hcomment'
	# gongfu.short_description ='功夫'
	def book(self):
		if self.hbook is None:
			return ''
		return self.hbook.btitle
	book.short_description ='图书名称'
	book.admin_order_field = 'hbook'

class AreaInfo(models.Model):
	atitle = models.CharField(max_length=30)
	aParent = models.ForeignKey('self',null=True,blank=True)

#class BookInfoManager(models.Manager):
#	def get_queryset(self):
#		return super(BookInfoManager,self).get_queryset().filter(isDelete=False)


class PicTest(models.Model):
# 定义一个属性，他的作用就是定义我们提交图片的位置
	pic = models.ImageField(upload_to='book_app/')
	def __str__(self):
		return self.pic.name


class GoodsInfo(models.Model):
    gcontent = HTMLField()
