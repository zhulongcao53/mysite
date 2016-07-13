#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField

class Host(models.Model):
    """store host information"""
    vendor = models.CharField(max_length=30,null=True)
    sn = models.CharField(max_length=30,null=True)
    product = models.CharField(max_length=30,null=True)
    cpu_model = models.CharField(max_length=50,null=True)
    cpu_num = models.CharField(max_length=2,null=True)
    cpu_vendor = models.CharField(max_length=30,null=True)
    memory_part_number = models.CharField(max_length=30,null=True)
    memory_manufacturer = models.CharField(max_length=30,null=True)
    memory_size = models.CharField(max_length=20,null=True)
    device_model = models.CharField(max_length=30,null=True)
    device_version = models.CharField(max_length=30,null=True)
    device_sn = models.CharField(max_length=30,null=True)
    device_size = models.CharField(max_length=30,null=True)
    osver = models.CharField(max_length=30,null=True)
    hostname = models.CharField(max_length=30,null=True)
    os_release = models.CharField(max_length=30,null=True)
    ipaddr = models.IPAddressField(max_length=15)
    def __unicode__(self):
        return self.hostname
        
    class Meta:
        verbose_name = "服务器信息"
        verbose_name_plural = "服务器信息"
        
class HostAdmin(admin.ModelAdmin):
    list_display = ['vendor',
        'sn',
        'product',
        'cpu_model',
        'cpu_num',
        'cpu_vendor',
        'memory_part_number',
        'memory_manufacturer',
        'memory_size',
        'device_model',
        'device_version',
        'device_sn',
        'device_size',
        'osver',
        'hostname',
        'os_release'
        ]

admin.site.register(Host, HostAdmin)

