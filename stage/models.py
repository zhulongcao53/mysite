#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField

# Create your models here.
class BasicInfo(models.Model):
    ipadd = models.IPAddressField(verbose_name = u'IP地址')
    cpu = models.CharField(max_length=255, blank=True, verbose_name = u'CPU%')
    mem = models.CharField(max_length=255, blank=True, verbose_name = u'内存%')
    disk = models.CharField(max_length=255, blank=True, verbose_name = u'磁盘%')
    sys_version = models.CharField(max_length=255, blank=True, verbose_name = u'操作系统')
    sys_bit = models.CharField(max_length=100, blank=True, verbose_name = u'32/64位')
    MAC = models.CharField(max_length=100, blank=True, verbose_name = u'MAC')
    
    def __unicode__(self):
        return self.ipadd
 
    class Meta:
        verbose_name = "服务器信息"
        verbose_name_plural = "服务器信息"

#主机组表，用来对主机进行分组
class HostGroup(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(BasicInfo)

    class Meta:
        verbose_name = "主机信息"
        verbose_name_plural = "主机信息"

class BasicInfo_admin(admin.ModelAdmin):

    list_display = ('ipadd', 'cpu', 'mem', 'disk', 'sys_version', 'sys_bit', 'MAC')
    list_filter = ('ipadd', )

class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(BasicInfo, BasicInfo_admin)
admin.site.register(HostGroup,HostGroupAdmin)
