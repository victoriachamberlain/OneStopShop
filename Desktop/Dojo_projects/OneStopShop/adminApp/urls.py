from django.urls import path
from . import views

urlpatterns = [
    # if no page numbers, it defaults to the 1st page
    path("orders/show/<int:orderId>", views.showOrderDetails),
    # path("orders/show/", views.showOrderDetails),

    path("dashboard/orders/<int:orderId>/edit", views.editOrderStatus),
    # if page numbers, it shows that page number
    path("dashboard/orders/<int:pageNum>", views.showOrders),
    # path("dashboard/orders/", views.showOrders),
    ###---
    path("product/delete/<int:orderId>", views.deleteProduct),
    ###---
    # path("product/show/<int:orderId>", views.showProduct),
    ###---
    path("product/edit/<int:orderId>", views.editProduct),
    path("product/create", views.createProduct),
    # if page numbers, it shows that page number
    path("dashboard/products/<int:pageNum>", views.showProducts),
    path("showProducts", views.showProducts),
    # if no page numbers, it defaults to the 1st page
    path("dashboard/products", views.showProducts),
    path("", views.admin_dash),
]
##------
# urlpatterns = [
#     path('', views.showLogin),

#     path('login', views.processLogin),
###_------------
