
from math import prod
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

from addpro.models import Order, OrderItem, Product



def make_payment(request):
    cart = request.session.get('cart', {})
    if cart:
        order = Order.objects.create()
        for pk, item in cart.items():
            product = get_object_or_404(Product, pk=pk)
            OrderItem.objects.create(order=order, product=product, quantity=item['quantity'], price=item['price'])
        request.session['cart'] = {}
        request.session.modified = True
        messages.info(request, 'Payment successful')
        print(f'Order {order.id} created with items: {order.items.all()}')  # Debug print
        return redirect('payment_success')
    else:
        messages.warning(request, 'Cart is empty')
        return redirect('cart')

def payment_success(request):
    return render(request, 'payment_success.html')

def view_orders(request):
    orders = Order.objects.all().prefetch_related('items__product')
    return render(request, 'orders.html', {'orders': orders})