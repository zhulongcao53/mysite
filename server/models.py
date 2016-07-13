#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin

class ServerInfo(models.Model):
    TYPE_SIZES = (
        ('W', 'Windows'),
        ('V', 'VNC'),
        ('R', 'Radmin'),
        ('S1', 'Sehll'),
        ('S2', 'Securecrt'),
        ('P', 'putty'),
    )
    ip = models.CharField(max_length=50,verbose_name = u'IP地址')
    type = models.CharField(max_length=5, choices=TYPE_SIZES, verbose_name = u'远程方式')
    port = models.CharField(max_length=50, verbose_name = u'端口')
    account = models.CharField(max_length=200, verbose_name = u'账号')
    password = models.CharField(max_length=200, verbose_name = u'密码')
    serverNO = models.CharField(max_length=200, verbose_name = u'主机名', null=True, blank=True)
    system = models.CharField(max_length=200, verbose_name = u'操作系统')
    time = models.CharField(max_length=50, verbose_name = u'购置时间')
    purpose = models.CharField(max_length=50, verbose_name = u'用途', null=True, blank=True)
    remarks = models.CharField(max_length=50, verbose_name = u'备注', null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.ip, self.time)

    class Meta:
        verbose_name = "服务器信息"
        verbose_name_plural = "服务器信息"

class cabinetInfo(models.Model):
    Warranty_SIZES = (
        ('Y', '是'),
        ('N', '否'),
    )
    cabinet = models.CharField(max_length=50,verbose_name = u'机柜')
    ip = models.CharField(max_length=50,verbose_name = u'IP地址')
    ip1 = models.CharField(max_length=50,verbose_name = u'内网IP')
    asset = models.CharField(max_length=100, verbose_name = u'资产号')
    time = models.CharField(max_length=50, verbose_name = u'购置时间')
    Warranty = models.CharField(max_length=5, choices=Warranty_SIZES, verbose_name = u'是否过保')
    remarks = models.CharField(max_length=50, verbose_name = u'备注', null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.ip, self.time)

    class Meta:
        verbose_name = "机柜信息"
        verbose_name_plural = "机柜信息"

class ServerInfoadmin(admin.ModelAdmin):
    list_display = ( 'ip', 'type', 'port', 'account', 'password', 'serverNO', 'system', 'time', 'purpose', 'remarks')
    list_filter = ('ip',)        # 过滤器
    search_fields = ('ip', 'account', 'serverNO') #快速查询栏
    ordering = ('-time',)

class cabinetInfoadmin(admin.ModelAdmin):
    list_display = ( 'cabinet', 'ip', 'ip1', 'asset', 'time', 'Warranty', 'remarks')
    list_filter = ('ip',)        # 过滤器
    search_fields = ('cabinet', 'ip', 'time') #快速查询栏
    ordering = ('-time',)

admin.site.register(ServerInfo,ServerInfoadmin) 
admin.site.register(cabinetInfo,cabinetInfoadmin)
