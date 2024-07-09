from math import prod
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

from addpro.models import Product

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