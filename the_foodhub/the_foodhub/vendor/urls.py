from django.urls import path

from the_foodhub.vendor.views import signup_vendor, vendor_profile, vendor_dashboard

urlpatterns = (
    path('', vendor_dashboard, name='vendor'),
    path('signup_vendor/', signup_vendor, name='signup_vendor'),
    path('vendor_dashboard/', vendor_dashboard, name="vendor_dashboard"),
    path('vendor_profile/', vendor_profile, name='vendor_profile'),
)