from django.urls import include, path

from user.views import UserRegisterViewSet, LogoutView, RetrieveUpdateProfileAPIView

urlpatterns = [
    path("register/", UserRegisterViewSet.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", RetrieveUpdateProfileAPIView.as_view(), name="profile"),
]

app_name = "user"