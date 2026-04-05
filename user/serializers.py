from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=validated_data.get("username", ""),
        )
        Profile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "username",
        )


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "date_of_birth",
            "location",
            "biography",
            "created_at",
            "updated_at",
            "is_private",
            "avatar"
        )