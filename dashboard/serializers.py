from rest_framework import serializers
from .models import *

class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = '__all__'