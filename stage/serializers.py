from stage.models import BasicInfo,HostGroup
from rest_framework import serializers

class BasicInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BasicInfo
        fields = ('ipadd', 'cpu', 'disk', 'mem', 'sys_version', 'sys_bit', 'MAC')


class HostGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostGroup
        fields = ('name', 'members')
