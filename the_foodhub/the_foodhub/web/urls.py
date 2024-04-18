from django.urls import path

from the_foodhub.web.views import index

urlpatterns = (
    path('', index, name='home'),
)