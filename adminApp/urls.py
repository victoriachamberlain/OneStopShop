from django.urls import path
from . import views

urlpatterns = [
    path("edit_product", views.edit_product),
    path("add_product", views.add_product),
    path("orders_dash", views.orders),
    path("manage_products", views.manage_products),
    path("", views.admin_dash),
]
