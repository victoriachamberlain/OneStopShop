from django.shortcuts import render, HttpResponse, redirect
from .models import *
from productsApp.models import *

def showLogin(request):
    return HttpResponse('admin login page') # render admin login page

def processLogin(request):
    # refer to login app's login function
    return HttpResponse('admin login process') # processes the login and redirects to dashboard/orders/1

def showOrders(reqeuest, pageNum):
    return HttpResponse('admin dashboard - orders') # render admin dashboard - orders

def editOrderStatus(request, orderId):
    # code for editing the order status of an order
    return HttpResponse('process order edit') # process the edit and redirect to page currently at

def showOrderDetails(request, orderId):
    return HttpResponse('order details') # render a page with all the details of the order

def showProducts(request):
    return HttpResponse('admin dashboard - products') # render admin dashboard - products

def createProduct(request):
    # code for creating a product object
    return HttpResponse('create a product') # process the creation and redirect to the products page

def showProduct(request, orderId):
    return HttpResponse('edit page with editable product info') # render edit product page

def editProduct(request, orderId):
    # code for processing the editing of the product object
    return HttpResponse('process product edit') # process the edit and redirect back to the product page previously at

def deleteProduct(request, orderId):
    # code for deleting the editing of the product object
    return HttpResponse('process product deletion') # process the deletion and redirect back to the  product page previously at
