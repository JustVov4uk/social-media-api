from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        token = RefreshToken(request.data["refresh"])
        token.blacklist()
        return Response(status=status.HTTP_204_NO_CONTENT)