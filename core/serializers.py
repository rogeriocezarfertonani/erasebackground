from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import EraseBackgroundModel


class EraseBackgroundSerializer(serializers.ModelSerializer):

    class Meta:
        model = EraseBackgroundModel
        fields = ('id', 'image')
