from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Session, Screenshot



class ScreenshotSerializer(serializers.ModelSerializer):
  screenshot = Base64ImageField() # From DRF Extra Fields

  class Meta:
    model = Screenshot
    fields = '__all__' 


class SessionSerializer(serializers.ModelSerializer):

  class Meta:
    model = Session
    screenshots = ScreenshotSerializer(many=True, read_only=True)
    fields = '__all__' 

