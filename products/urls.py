from django.urls import path
from products.views import products_view, categories_view

urlpatterns = [
    path('products/', products_view),
    path('categories/', categories_view)
]
