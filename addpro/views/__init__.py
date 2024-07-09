from .product_views import viewproduct, addproduct, product_detail
from .order_views import make_payment, view_orders , payment_success
from .cart_views import add_to_cart,cart,update_cart,remove_from_cart
from .save_for_later import save_later_product,save_for_later,saved_for_later
from .login_views import register,login,logout

__all__ = ['viewproduct', 'addproduct', 'product_detail', 'make_payment', 'view_orders', 'payment_success',
           'add_to_cart','cart','update_cart','remove_from_cart',
           'save_later_product','save_for_later','saved_for_later',
           'register','login','logout']
