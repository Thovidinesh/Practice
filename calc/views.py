from django.shortcuts import render
from django.http import HttpResponse

#from .models import product
# Create your views here.
def master(request):
    return render(request,'master.html',)