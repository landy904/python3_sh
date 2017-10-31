from django.db import models
from db.BaseModel import *
from utils.wrappers import *
from utils.common import *

# Create your models here.
class UserManager(models.Manager):
    def get_userinfo_byname(self,username):
        try:
            return self.get(user_name = username)
        except User.DoesNotExist:
            return None

    #注册信息入库
    def register_userinfo_save(self,request):
        user_name = post(request,'user_name')
        user_pass = post(request,'user_pass1')
        user_mail = post(request,'user_mail')
        user = User()
        user.user_name = user_name
        user.user_pass = passwd_jiami(user_pass)
        user.user_mail = user_mail
        user.save()


class User(BaseModel):
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_pass = models.CharField(max_length=64,verbose_name='密码')
    user_mail = models.CharField(max_length=30,verbose_name='邮箱')
    user_active = models.BooleanField(default=False)
    user_recv = models.CharField(max_length=30,verbose_name='收件人')
    user_address = models.CharField(max_length=80,verbose_name='地址')
    user_code = models.CharField(max_length=6,verbose_name='邮编')
    user_tele = models.CharField(max_length=11,verbose_name='手机')

    objects = UserManager()
