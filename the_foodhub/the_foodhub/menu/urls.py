from django.urls import path

from the_foodhub.menu.views import menu_builder, add_category, edit_category, delete_category, add_food, edit_food, \
    delete_food

urlpatterns = [
    path('menu-builder/', menu_builder, name='menu_builder'),

    # Category CRUD
    path('menu-builder/category/add/', add_category, name='add_category'),
    path('menu-builder/category/edit/<int:pk>/', edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/', delete_category, name='delete_category'),

    # FoodItem CRUD
    path('menu-builder/food/add/', add_food, name='add_food'),
    path('menu-builder/food/edit/<int:pk>/', edit_food, name='edit_food'),
    path('menu-builder/food/delete/<int:pk>/', delete_food, name='delete_food'),
]