from django.urls import path
from the_foodhub.accounts.views import (
    signup_user, signin_user, signout_user, customer_dashboard, my_account,
    vendor_dashboard, activate, forgot_password, reset_password_validate,reset_password,
)

urlpatterns = (
    path("signup_user/", signup_user, name="signup_user"),
    path("signin_user/", signin_user, name="signin_user"),
    path("signout_user/", signout_user, name="signout_user"),
    path("my_account/", my_account, name="my_account"),
    path('customer_dashboard/', customer_dashboard, name="customer_dashboard"),
    path('vendor_dashboard/', vendor_dashboard, name="vendor_dashboard"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name="reset_password_validate"),
    path('reset_password/', reset_password, name="reset_password"),
)
