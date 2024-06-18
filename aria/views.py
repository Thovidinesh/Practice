from django.shortcuts import render
from .models import products

def index(request):
    pros=products.objects.all()
    return render(request, 'index.html',{'pros':pros})

