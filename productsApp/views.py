from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
    	# "User": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "index.html", context)

def showProduct(request): #add productID
    context = {
    	# "User": User.objects.get(id=request.session['user_id']),
        # "Product": Product.objects.all()
    }
    return render(request, "productPage.html", context)

def showShoppingCart(request):#add userId
    context = {
    	# "User": User.objects.filter(id=userID),
        # "Product": Product.objects.all()
    }
    return render(request, "shoppingCart.html", context)

def showPayment(request):#add UserId
    context = {
    	# "User": User.objects.filter(id=userID),
        # "Product": Product.objects.filter(id=userId)
    }
    return render(request, "payment.html", context)# render payment page with all of the items from shopping cart

def processPayment(request, userId):
    # code to process payment
    return HttpResponse('process payment') # process the payment and redirect to the receipt page

def showReceipt(request, orderId):
    context = {
    	# "User": User.objects.filter(id=userID),
        # "Order": Order.objects.filter(id=orderId)
    }
    return render(request, "receipt.html", context)
    return HttpResponse('receipt page') # render receipt page with the order information

def showWishList(request, userId):
    context = {
    	# "User": User.objects.filter(id=userID),
    }
    return render(request, "wishList.html", context)
    return HttpResponse('wish list page') # render wish list page with all the products and qty