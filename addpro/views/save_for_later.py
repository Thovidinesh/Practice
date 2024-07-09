from math import prod
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

from addpro.models import Order, OrderItem, Product


def save_later_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def save_for_later(request, pk):
    cart = request.session.get('cart', {})
    saved_for_later = request.session.get('saved_for_later', {})
    if str(pk) in cart:
        saved_for_later[str(pk)] = cart[str(pk)]
        del cart[str(pk)]
        request.session['cart'] = cart
        request.session['saved_for_later'] = saved_for_later
        messages.info(request, 'Product saved for later')
    else:
        messages.warning(request, 'Product not found in cart')
    return redirect('viewproduct')





def saved_for_later(request):
    saved_items = request.session.get('saved_for_later', {})
    saved_products = []
    for pk, item in saved_items.items():
        product = get_object_or_404(Product, pk=int(pk))
        saved_products.append({
            'pk': pk,
            'name': product.name,
            'img': product.img.url if product.img else None,
            'price': item['price'],
            'quantity': item['quantity']
        })
    return render(request, 'save_to_later.html', {'saved_products': saved_products})
