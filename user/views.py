from rest_framework.decorators import action
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import Profile, User
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


class ListProfileAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Profile.objects.all()
        search = self.request.query_params.get("search", None)
        if search:
            queryset = queryset.filter(
                Q(user__username__icontains=search) | Q(user__email__icontains=search)
            )
        return queryset


class FollowViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    @action(
        detail=True,
        methods=["post"],
        permission_classes=(IsAuthenticated,),
    )
    def follow(self, request, pk):
        user = self.get_object()
        if request.user == user:
            return Response(
                {"error": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.user.following.add(user)
        return Response(status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=(IsAuthenticated,),
    )
    def unfollow(self, request, pk):
        user = self.get_object()
        if request.user == user:
            return Response(
                {"error": "You cannot unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.user.following.remove(user)
        return Response(status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=(IsAuthenticated,),
    )
    def followers(self, request):
        followers = request.user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=(IsAuthenticated,),
    )
    def following(self, request):
        following = request.user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)