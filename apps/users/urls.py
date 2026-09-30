from django.urls import path

from .views import (
    RegisterView,
    MeView,
    MyProfileView,
    UpdateMeview,
    ChangePasswordView
)

urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),
    path("me/update/", UpdateMeview.as_view,name="me-update"),
    path("change-password/", ChangePasswordView.as_view,name="change_password"),
    path(
        "profile/",
        MyProfileView.as_view(),
        name="profile",
    ),
]