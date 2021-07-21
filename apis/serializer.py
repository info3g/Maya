from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

# class ReactSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['username','password']
	

class ReactSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['email','password']



class InstagramSerializer(serializers.Serializer):
    username = serializers.CharField()
    email  = serializers.CharField()
    password  = serializers.CharField()
    likecount  = serializers.CharField()
    viewcount  = serializers.CharField()
    followercount  = serializers.CharField()
