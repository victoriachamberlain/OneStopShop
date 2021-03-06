from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('products/<str:categoryName>', views.products),
    path('product/<int:productId>', views.singleProduct),
    path('product/<int:productId>/addToCart', views.addToCart),
    path('user/<int:userId>/shoppingCart', views.shoppingCart),
    path('user/<int:userId>/shoppingCart/<int:productId>/delete', views.deleteCartItem),
    path('user/<int:userId>/payment', views.showPayment),
    path('user/<int:userId>/payment/process', views.processPayment),
    path('user/<int:userId>/wishList', views.wishList),
    path('user/<int:userId>/wishList/add', views.addWishItem),
    path('user/<int:userId>/wishList/<int:productId>/delete', views.deleteWishItem),
    path('user/<int:userId>/wishList/<int:productId>/addToCart', views.addWishToCart),
    path('<int:orderId>/receipt', views.showReceipt),
]