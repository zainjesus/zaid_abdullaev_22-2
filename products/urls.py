from django.urls import path
from products.views import ProductsView, CategoriesView, DetailProductView, ProductCreateView

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('products/<int:id>/', DetailProductView.as_view()),
    path('products/create/', ProductCreateView.as_view())
]
