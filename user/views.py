from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import Profile
from user.serializers import UserSerializer, UserRegisterSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        token = RefreshToken(request.data["refresh"])
        token.blacklist()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RetrieveUpdateProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class RetrieveProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(Profile, user=self.kwargs["pk"])
