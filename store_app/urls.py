from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.register_user),
    path('login', views.login),
    path('success', views.success),
    path('log_out', views.log_out),
    path('account_information', views.account_information),
    path('action', views.action),
    path('comedy', views.comedy),
    path('drama', views.drama),
    path('electronics', views.electronics),
    path('scifi', views.scifi),
    path('cart/<int:item_id>', views.cart),
    path('add_to_cart/<int:item_id>', views.add_to_cart),
    path('delete/<int:item_id>', views.delete),
    path('main_cart', views.main_cart),
    path('checkout', views.checkout)
]