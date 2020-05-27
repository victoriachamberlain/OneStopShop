from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    return HttpResponse('hello') # render main page

def showProduct(request, productId):
    # include context dictionary to pass in a product object
    return HttpResponse('product detail') # render product detail page

def showShoppingCart(request, userId):
    # include context dictionary to pass the shopping cart object linked to the user
    return HttpResponse('shopping cart') # render shopping cart page

def showPayment(request, userId):
    return HttpResponse('payment page') # render payment page with all of the items from shopping cart

def processPayment(request, userId):
    # code to process payment
    return HttpResponse('process payment') # process the payment and redirect to the receipt page

def showReceipt(request, orderId):
    # include context dictionary to pass in the order object
    return HttpResponse('receipt page') # render receipt page with the order information

def showWishList(request, userId):
    # include context dictionary to pass the wish list object linked to the user
    return HttpResponse('wish list page') # render wish list page with all the products and qty
