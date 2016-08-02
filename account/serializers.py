# -*- coding: utf-8 -*-
# author: jeremy
from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import UserProfile
from rest_framework.authtoken.models import Token


class UserRegisterSerializer(serializers.Serializer):
    TYPE = (
        (0, u'网站用户'),
        (1, u'手机用户'),
    )
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(min_length=6, required=True)
    email = serializers.EmailField(required=False, allow_blank=True, allow_null=True)
    type = serializers.ChoiceField(choices=TYPE, default=0)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('name', 'telephone', 'type')


class AuthUserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'user_profile.name')

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        email = validated_data.pop('email', '')
        user = User.objects.create_user(username, password=password, email=email, **validated_data)

        return user


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='auth_user.username')
    password = serializers.CharField(source='auth_user.password')

    class Meta:
        model = UserProfile
        fields = ('name', 'telephone', 'type', 'username', 'password')
