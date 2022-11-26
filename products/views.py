from django.shortcuts import render, redirect
from products.models import Product, Category, Review
from products.forms import ProductCreateForm, ReviewCreateForm


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
            'reviews': reviews,
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=data)

    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                product_id=id,
                grade=form.cleaned_data.get('grade'),
            )
            return redirect(f'/products/{id}/')
        else:
            product = Product.objects.get(id=id)
            reviews = Review.objects.filter(product_id=id)

            data = {
                'product': product,
                'categories': product.category.all(),
                'reviews': reviews,
                'form': form
            }

            return render(request, 'products/detail.html', context=data)


def product_create_view(request):
    if request.method == 'GET':
        data = {
            'form': ProductCreateForm
        }

        return render(request, 'products/create.html', context=data)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                seller_id=1,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                characteristics=form.cleaned_data.get('characteristics'),
                price=form.cleaned_data.get('price')
            )
            return redirect('/products')
        else:
            data = {
                'form': form
            }
            return render(request, 'products/create.html', context=data)
