from django.contrib import admin
from .models import *
# Register your models here.
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date','bread','bcomment','isDelete']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 6
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','isDelete','hbook']
    list_per_page = 6
    actions_on_bottom = True
    list_filter = ['hbook']
    search_fields = ['hname']

# def BookStackedInline(admin.StackedInline):
#     model = HeroInfo
#     extra = 1
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display =['id']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(PicTest)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
