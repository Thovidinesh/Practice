from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('books',views.books),
    # path('books/<int:pk>',views.book),
]
