from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views
from . import views
from . import socialaccounts
from . import emailconfirm

app_name = "users"

router = routers.SimpleRouter()
router.register(r"users", views.UserViewSet)


confirmpatterns = [
    path(
        "activate/<str:uid64>/<str:token>",
        emailconfirm.activate,
        name="activate",
    ),
    path(
        "reset_mail/",
        emailconfirm.reset_password_sendmail,
        name="reset_mail",
    ),
    path(
        "reset_passwd/",
        views.reset_password,
        name="reset_passwd",
    ),
]

urlpatterns = [
    path("users/", include(confirmpatterns)),
    path("users/my_info/", views.get_info),
    path("users/auth/google/callback", socialaccounts.google_callback),
    path("users/auth/kakao/callback", socialaccounts.kakao_callback),
    path("users/auth/naver/callback", socialaccounts.naver_callback),
    path("users/val_email/", views.validate_email),
    path("users/val_nickname/", views.validate_nickname),
    path("users/change-password", views.change_password),
    path("users/Refresh/", TokenRefreshView.as_view()),
    path("users/register_user/", views.register_user),
    path("", include(router.urls)),
]
