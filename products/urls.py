from django.urls import path
from products.views import products_view, categories_view, detail_product_view, product_create_view

urlpatterns = [
    path('products/', products_view),
    path('categories/', categories_view),
    path('products/<int:id>/', detail_product_view),
    path('products/create/', product_create_view)

]
