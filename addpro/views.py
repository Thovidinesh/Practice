
from math import prod
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

from addpro.models import Order, OrderItem, Product

# Create your views here.
def viewproduct(request):
    products = Product.objects.all()
    return render(request, 'viewproduct.html',{'products': products})



def addproduct(request):
    if request.method == 'POST':
        name=request.POST['name']
        img=request.FILES.get('image')
        if img:
            pass
        else:
            pass
        desc=request.POST.get('desc','')
        price = request.POST.get('price')
        if name and img and desc and price:
            prod = Product.objects.create(name=name, img=img, desc=desc, price=price)
            prod.save()
            messages.success(request, 'Successfully added product.')
            return redirect('viewproduct')
        return redirect( 'addproduct')
    return render(request,'addproduct.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


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


def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
        messages.info(request, 'Product removed from cart')
    else:
        messages.warning(request, 'Product not found in cart')
    return redirect('cart')


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