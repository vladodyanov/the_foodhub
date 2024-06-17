from django.urls import path

from the_foodhub.menu.views import menu_builder

urlpatterns = [
    path('menu-builder/', menu_builder, name='menu_builder'),
]