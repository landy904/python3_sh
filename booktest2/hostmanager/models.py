#coding:utf-8
from django.db import models


# Create your models here.
# class HostGroup(models.Model):
#     hgid = models.AutoField(primary_key=True)
#     host_id = models.ForeignKey('Host')
#     group_id = models.ForeignKey('Group')
#
#
# class Host(models.Model):
#     hid = models.AutoField(primary_key=True)
#     hostname = models.CharField(max_length=32)
#     ip = models.CharField(max_length=32)
#
#
# class Group(models.Model):
#     gid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=16)
#     # 指定第三张表
#     h2g = models.ManyToManyField('Host', through='HostGroup')

#class Host(models.Model):
#    hid = models.AutoField(primary_key=True)
#    hostname = models.CharField(max_length=32)
#    ip = models.CharField(max_length=32)


#class Group(models.Model):
#    gid = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=16)
#    # 任意一个字段，会自动生成第三张表，且第三张表会自动的添加联合唯一索引，Unique
#    h2g = models.ManyToManyField('Host')
