# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from stage.models import BasicInfo,HostGroup
from rest_framework import viewsets
from stage.serializers import BasicInfoSerializer, HostGroupSerializer

# Create your views here.
#包含json模块
try:
    import json
except ImportError,e:
    import simplejson as json
#用来接收客户端服务器发送过来的数据
def collect(request):
    req = request
    if req.POST:
        ipadd = req.POST.get('ip')
        cpu = req.POST.get('cpu')
        disk = req.POST.get('disk')
        mem = req.POST.get('mem')
        sys_version = req.POST.get('sys_version')
        sys_bit = req.POST.get('sys_bit')
        MAC = req.POST.get('MAC')
        host = BasicInfo()
        host.ipadd = ipadd
        host.cpu = cpu
        host.mem = mem
        host.disk = disk
        host.sys_version = sys_version
        host.sys_bit = sys_bit
        host.MAC = MAC
        host.save()       #将客户端传过来的数据通过POST接收，存入数据库
        return HttpResponse('OK')   #如果插入成功，返回'ok'
    else:
        return HttpResponse('no post data')
#提供给NAGIOS 的API
def gethosts(req):
    d = []
    hostgroups = HostGroup.objects.all()
    for hg in hostgroups:
        ret_hg = {'hostgroup':hg.name,'members':[]}
        members = hg.members.all()
        for h in members:
            ret_h = {'ipadd':h.ipadd
            }
            ret_hg['members'].append(ret_h)
        d.append(ret_hg)
    ret = {'status':0,'data':d,'message':'ok'}
    return HttpResponse(json.dumps(ret))

class BasicInfoViewSet(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all()
    serializer_class = HostGroupSerializer
