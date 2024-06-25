from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewproduct, name='viewproduct'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('Products/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('update_cart/<int:pk>/<str:action>/', views.update_cart, name='update_cart'),
    path('save-for-later/<int:pk>/', views.save_for_later, name='save_for_later'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('saved-for-later/', views.saved_for_later, name='saved_for_later'),
    path('product/<int:pk>/', views.save_later_product, name='save_later_product'),
    path('make-payment/', views.make_payment, name='make_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('orders/', views.view_orders, name='view_orders'),
    path('view-orders/', views.view_orders, name='view_orders'), 
]
