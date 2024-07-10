from django.urls import path
from django.urls import path
from .views import viewproduct, addproduct, product_detail
from .views import add_to_cart, cart, update_cart, remove_from_cart
from .views import make_payment, payment_success, view_orders
from .views import save_for_later, save_later_product, saved_for_later
from .views import register,login,logout

urlpatterns = [
    path('', viewproduct, name='viewproduct'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('addproduct/', addproduct, name='addproduct'),
    path('Products/<int:pk>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('update_cart/<int:pk>/<str:action>/', update_cart, name='update_cart'),
    path('save-for-later/<int:pk>/', save_for_later, name='save_for_later'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('saved-for-later/', saved_for_later, name='saved_for_later'),
    path('product/<int:pk>/', save_later_product, name='save_later_product'),
    path('make-payment/', make_payment, name='make_payment'),
    path('payment-success/', payment_success, name='payment_success'),
    path('orders/', view_orders, name='view_orders'),
    path('view-orders/', view_orders, name='view_orders'), 
]
