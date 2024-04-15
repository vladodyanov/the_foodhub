from django.urls import path
from the_foodhub.accounts.views import SignInUserView,  SignUpUserView, signout_user

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),
)
