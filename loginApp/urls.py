from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    # path('login', views.login),
    path('myaccount/<int:userId>', views.editUser),
    path('myaccount/<int:userId>/update', views.updateUser),
    path('logout', views.logout)
]