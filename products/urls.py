from django.urls import path, include
from products.views import get_product

urlpatterns = [
    path('<slug>/', get_product, name='get_product'),
]
