from django.shortcuts import render
from products.models import Product, Category, Review


def products_view(request):
    if request.method == "GET":
        category_id = request.GET.get('category_id')
        if category_id:
            products = Product.objects.filter(category__in=[category_id])
        else:
            products = Product.objects.all()

        products = [{
            'id': product.id,
            'image': product.image,
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'characteristics': product.characteristics,
            'categories': product.category.all()
        } for product in products]

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)


def categories_view(request, **kwargs):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=data)


def detail_product_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        reviews = Review.objects.filter(product_id=id)

        data = {
            'product': product,
            'categories': product.category.all(),
            'reviews': reviews
        }

        return render(request, 'products/detail.html', context=data)
