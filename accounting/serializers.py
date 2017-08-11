from rest_framework import serializers
from .models import *


class RecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'record_detail_view'}
        }