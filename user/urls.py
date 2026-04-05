from django.urls import include, path

from user.views import UserRegisterViewSet, LogoutView, RetrieveUpdateProfileAPIView, RetrieveProfileAPIView, \
    ListProfileAPIView

urlpatterns = [
    path("register/", UserRegisterViewSet.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", RetrieveUpdateProfileAPIView.as_view(), name="profile"),
    path("profile/search/", ListProfileAPIView.as_view(), name="profile-search"),
    path("profile/<int:pk>/", RetrieveProfileAPIView.as_view(), name="profile-detail"),
]

app_name = "user"