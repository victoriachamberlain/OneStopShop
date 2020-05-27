from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('products/show/<int:productId>', views.showProduct),
    path('user/<int:userId>/shoppingCart', views.showShoppingCart),
    path('user/<int:userId>/payment', views.showPayment),
    path('user/<int:userId>/payment/process', views.processPayment),
    path('<int:orderId>/receipt', views.showReceipt),
    path('user/<int:userId>/wishList', views.showWishList),
]