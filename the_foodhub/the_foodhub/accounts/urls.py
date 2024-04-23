from django.urls import path
from the_foodhub.accounts.views import (signup_user, signin_user, signout_user, customer_dashboard, my_account,
                                        vendor_dashboard)

urlpatterns = (
    path("signup_user/", signup_user, name="signup_user"),
    path("signin_user/", signin_user, name="signin_user"),
    path("signout_user/", signout_user, name="signout_user"),
    path("my_account/", my_account, name="my_account"),
    path('customer_dashboard/', customer_dashboard, name="customer_dashboard"),
    path('vendor_dashboard/', vendor_dashboard, name="vendor_dashboard"),
)
