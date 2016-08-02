# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserRegisterSerializer, UserProfileSerializer, AuthUserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from account.models import UserProfile

from rest_framework import generics, mixins


class UserRegister(APIView):
    permission_classes = (permissions.BasePermission,)

    def post(self, request, format=None):
        resutl = {}
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            email = serializer.validated_data.get('email')
            type = serializer.validated_data.get('type', 0)
            auth_user = User()
            auth_user.username = username
            auth_user.set_password(password)
            auth_user.email = email
            auth_user.save()

            # 保存user扩展
            userProfile = UserProfile()
            userProfile.user = auth_user
            userProfile.telephone = username
            userProfile.type = type
            userProfile.save()

            return Response({'status': 'ok'})


class CreateUserProfile(generics.ListCreateAPIView):
    permission_classes = (permissions.BasePermission,)
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
    raise_exception = True


class MyUserProfile(generics.CreateAPIView):
    permission_classes = (permissions.BasePermission,)
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    raise_exception = True


def index(request):

    return render(request, 'index.html', {})

