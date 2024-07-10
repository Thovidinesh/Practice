from math import prod
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

from addpro.models import Order, OrderItem, Product


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {} 
    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1
    else:
        cart[str(pk)] = {
            'name': product.name,
            'img': product.img.url,  # Store the image URL
            'price': str(product.price),
            'quantity': 1
        }
    request.session['cart'] = cart
    request.session.modified = True
    messages.info(request, 'Product added to cart')
    return redirect('cart')



def cart(request):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {} 
    total_items = sum(product['quantity'] for product in cart.values())
    total_price = sum(float(product['price']) * product['quantity'] for product in cart.values())
    final_price=total_price+(total_price*0.18)
    cart_items = []
    for pk, product in cart.items():
        cart_items.append({
            'pk': pk,
            'name': product['name'],
            'img': product.get('img', ''),  # Ensure this is correctly set to the image URL
            'price': product['price'],
            'quantity': product['quantity']
        })
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_items': total_items, 'total_price': total_price,'final_price':final_price})



def update_cart(request, pk, action):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {} 
    if str(pk) in cart:
        if action == 'increase':
            cart[str(pk)]['quantity'] += 1
        elif action == 'decrease':
            cart[str(pk)]['quantity'] -= 1
            if cart[str(pk)]['quantity'] <= 0:
                del cart[str(pk)]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
        messages.info(request, 'Product removed from cart')
    else:
        messages.warning(request, 'Product not found in cart')
    return redirect('cart')