from django.urls import path
from the_foodhub.accounts.views import SignInUserView

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
)
