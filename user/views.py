from django.shortcuts import render
from rest_framework import viewsets, generics

from user.serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
