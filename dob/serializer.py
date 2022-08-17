from .models import Wishes
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishes
        fields = "__all__"