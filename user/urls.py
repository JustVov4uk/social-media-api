from django.urls import include, path

from user.views import UserRegisterViewSet


urlpatterns = [
    path("register/", UserRegisterViewSet.as_view(), name="register"),
]

app_name = "user"