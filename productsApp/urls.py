from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('product', views.showProduct),
    path('shoppingCart', views.showShoppingCart),
    path('payment', views.showPayment),
    path('user/<int:userId>/payment/process', views.processPayment),
    path('<int:orderId>/receipt', views.showReceipt),
    path('user/<int:userId>/wishList', views.showWishList),
]