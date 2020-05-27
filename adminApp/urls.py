from django.urls import path
from . import views

urlpatterns = [
    path('', views.showLogin),
    path('login', views.processLogin),
    # if page numbers, it shows that page number
    path('dashboard/orders/<int:pageNum>', views.showOrders),
    # if no page numbers, it defaults to the 1st page
    path('dashboard/orders', views.showOrders),
    path('dashboard/orders/<int:orderId>/edit', views.editOrderStatus),
    path('orders/show/<int:orderId>', views.showOrderDetails),
    # if page numbers, it shows that page number
    path('dashboard/products/<int:pageNum>', views.showProducts),
    # if no page numbers, it defaults to the 1st page
    path('dashboard/products', views.showProducts),
    path('product/create', views.createProduct),
    path('product/show/<int:orderId>', views.showProduct),
    path('product/edit/<int:orderId>', views.editProduct),
    path('product/delete/<int:orderId>', views.deleteProduct),

]