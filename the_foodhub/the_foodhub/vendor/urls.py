from django.urls import path

from the_foodhub.vendor.views import signup_vendor

urlpatterns = (
    path("signup_vendor/", signup_vendor, name="signup_vendor"),
)