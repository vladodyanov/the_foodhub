from django.urls import path
from the_foodhub.accounts.views import SignInUserView,  SignUpUserView, signout_user

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup_user"),
    path("signin/", SignInUserView.as_view(), name="signin_user"),
    path("signout/", signout_user, name="signout_user"),
)
