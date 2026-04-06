from django.urls import include, path
from rest_framework.routers import DefaultRouter

from user.views import UserRegisterViewSet, LogoutView, RetrieveUpdateProfileAPIView, RetrieveProfileAPIView, \
    ListProfileAPIView, FollowViewSet

router = DefaultRouter()
router.register("follow", FollowViewSet, basename="follow")
urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegisterViewSet.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", RetrieveUpdateProfileAPIView.as_view(), name="profile"),
    path("profile/search/", ListProfileAPIView.as_view(), name="profile-search"),
    path("profile/<int:pk>/", RetrieveProfileAPIView.as_view(), name="profile-detail"),
]

app_name = "user"