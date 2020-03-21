from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url('cart_details/', views.cart_detail, name='cart_detail'),
    url('cart_add/', views.cart_add, name='cart_add'),
    url('cart_remove/', views.cart_remove, name='cart_remove'),
]

