from django.shortcuts import render, HttpResponse, redirect

def admin_dash(request):
    return render(request, "user_admin.html")

def manage_products(request):
    return render(request, "manage_products.html")

def orders(request):
    return render(request, "orders_dash.html")

def add_product(request):
    return render(request, "add_product.html")

def edit_product(request):
    return render(request, "edit_product.html")