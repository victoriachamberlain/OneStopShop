from django.db import models
from loginApp.models import *
from adminApp.models import *

# class ShippingInfo(models.Model):
#     first_name = models.CharField(max_length = 30)
#     last_name = models.CharField(max_length = 30)
#     address = models.CharField(max_length = 50)
#     address2 = models.CharField(max_length = 50)
#     city = models.CharField(max_length = 30)
#     state = model.CharField(max_length = 30)
#     zipcode = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class BillingInfo(models.Model):
#     first_name = models.CharField(max_length = 30)
#     last_name = models.CharField(max_length = 30)
#     address = models.CharField(max_length = 50)
#     address2 = models.CharField(max_length = 50)
#     city = models.CharField(max_length = 30)
#     state = model.CharField(max_length = 30)
#     zipcode = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

class Order(models.Model):
    user = models.ForeignKey(User, related_name = 'orders', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # one to many relationship with product

class WishList(models.Model):
    user = models.OneToOneField(User, related_name = 'wishList', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # one to many relationship with product

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, related_name = 'shoppingCart', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # one to many relationship with product

class Category(models.Model):
    name = models.CharField(max_length = 50)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # one to many relationship with product

class Product(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    order = models.ForeignKey(Order, related_name = 'products', on_delete = models.CASCADE)
    wishList = models.ForeignKey(WishList, related_name = 'products', on_delete = models.CASCADE)
    shoppingCart = models.ForeignKey(ShoppingCart, related_name = 'products', on_delete = models.CASCADE)
    category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
