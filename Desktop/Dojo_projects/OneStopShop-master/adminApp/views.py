from django.shortcuts import render, HttpResponse, redirect
from .models import *

def admin_dash(request):
    return render(request, "user_admin.html")

def showProducts(request):
    return render(request, "show_products.html")

## ORDERs and ORDER STATUS below
def showOrders(request, pageNum):
# def showOrders(request):
    return render(request, "showOrders.html")

def editOrderStatus(request, orderId):# code for editing the order status of an order
    return HttpResponse('process order edit') # process the edit and redirect to page currently at

# def showOrderDetails(request, orderId):
def showOrderDetails(request):
    return render(request, "showOrderDetails.html") # render a page with all the details of the order

### CREATE Products BELOW
def createProduct(request):# code for creating a product object
    return render(request, "add_product.html")

def editProduct(request, orderId):# code for processing the editing of the product object
    return render(request, "editProduct.html")

def deleteProduct(request, orderId): # code for deleting the editing of the product object
    return HttpResponse('process product deletion') # process the deletion and redirect back to the  product page previously at



####---------------------
# def showLogin(request):
#     return HttpResponse('admin login page') # render admin login page

# def processLogin(request):
#     # refer to login app's login function
#     return HttpResponse('admin login process') # processes the login and redirects to dashboard/orders/1
#-------------
