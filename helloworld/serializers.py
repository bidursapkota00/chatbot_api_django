from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .ai import *
from .models import Input


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ('id', 'input', 'output')


    

class IdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ('id')