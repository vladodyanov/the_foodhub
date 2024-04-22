from django.urls import path
from the_foodhub.accounts.views import signup_user, signin_user, signout_user, dashboard

urlpatterns = (
    path("signup_user/", signup_user, name="signup_user"),
    path("signin_user/", signin_user, name="signin_user"),
    path("signout_user/", signout_user, name="signout_user"),
    path('dashboard/', dashboard, name="dashboard")
)
