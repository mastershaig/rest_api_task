from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.UserRegistrationView.as_view(), name="signup"),
    path("signin/", views.UserLoginView.as_view(), name="signin"),
    path("user/", views.UserView.as_view(), name="get_user"),
]
