from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    return HttpResponse('hello') # render main page

def showProduct(request, productId):
    # include context dictionary to pass in a product object
    return HttpResponse('product detail') # render product detail page

def showPayment(request, userId):
    return HttpResponse('payment page') # render payment page with all of the items from shopping cart

def processPayment(request, userId):
    # code to process payment
    return HttpResponse('process payment') # process the payment and redirect to the receipt page

## Wish List
def wishList(request, userID):
    # include context dictionary to pass the wish list object linked to the user
    return HttpResponse("wish_list.html")

def addWishItem(request, WishList_id):
    WishList.objects.get(id=wishList_id).products.add(Product.objects.get(id=request.POST['product_id']))

    return redirect('/wishlist')

def deleteWishItem(request, product_id):
    to_delete=wishList.objects.get(id=product_id)
    to_delete.delete()
    return redirect('/wishlist')

def addWishtoCart(request, ShoppingCart_id):
    ShoppingCart.objects.get(id=ShoppingCart_id).products.add(Product.objects.get(id=request.POST['product_id']))

    return redirect('/wishlist')
    ##this cannot be right...

##Shopping Cart
def shoppingCart(request, user_id):
    # include context dictionary to pass the shopping cart object linked to the user
    return HttpResponse("shopping_cart.html")

def deleteCartItem(request, product_id):
    to_delete=ShoppingCart.objects.get(id=product_id)
    to_delete.delete()
    return redirect('/shoppingcart')

def addToCart(request, ShoppingCart_id):
     ShoppingCart.objects.get(id=ShoppingCart_id).products.add(Product.objects.get(id=request.POST['product_id']))

    return redirect('/shoppingcart')

##Receipt
def receipt(request, order_id):
    context={
        "purchased_items": Order.objects.get(id=order_id)
    }
    return HttpResponse('receipt.html')