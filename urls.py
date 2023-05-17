from django.urls import path
from . import views

urlpatterns = [
    path('api/products/<int:product_id>', views.get_product, name='get_product'),
    path('api/cart/add', views.add_to_cart, name='add_to_cart'),
    path('api/orders/place', views.place_order, name='place_order'),
]
