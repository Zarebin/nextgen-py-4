from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')
