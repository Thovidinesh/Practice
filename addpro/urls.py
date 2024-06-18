from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewproduct, name='viewproduct'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('Products/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('update_cart/<int:pk>/<str:action>/', views.update_cart, name='update_cart'),
]
