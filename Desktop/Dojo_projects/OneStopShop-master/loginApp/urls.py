from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.showLogin),
    path('register/', views.showRegister),
    path('process/register', views.register),
    path('process/login', views.login),
    path('myaccount/<int:userId>', views.editUser),
    path('myaccount/<int:userId>/<str:updateType>/update', views.updateUser),
    path('logout', views.logout)
]