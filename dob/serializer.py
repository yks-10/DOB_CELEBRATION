from .models import Wishes, SongDedication, Memories
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

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongDedication
        fields = "__all__"
class MemoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memories
        fields = "__all__"