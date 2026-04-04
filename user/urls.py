from django.urls import include, path

from user.views import UserRegisterViewSet, LogoutView

urlpatterns = [
    path("register/", UserRegisterViewSet.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

app_name = "user"