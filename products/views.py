from django.shortcuts import render, redirect
from products.models import Product, Category, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from users.utils import get_user_from_request
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, View
from django.views.generic.detail import DetailView

PAGINATION_LIMIT = 1


class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        return {
            'products': kwargs['products'],
            'user': get_user_from_request(self.request),
            'max_page': range(1, kwargs['max_page']+1)
        }

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = Product.objects.filter(category__in=[category_id])
        else:
            products = Product.objects.all()

        if search_text:
            products = products.filter(title__icontains=search_text)

        products = [{
            'id': product.id,
            'image': product.image,
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'characteristics': product.characteristics,
            'categories': product.category.all()
        } for product in products]

        max_page = round(products.__len__() / PAGINATION_LIMIT)
        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        return render(request, self.template_name, context=self.get_context_data(
            products=products,
            max_page=max_page
        ))


class CategoriesView(ListView):
    model = Category
    template_name = 'categories/categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'categories': self.get_queryset(),
            'user': get_user_from_request(self.request)
        }


class ProductCreateView(ListView, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'user': get_user_from_request(self.request),
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                seller_id=request.user.id,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                characteristics=form.cleaned_data.get('characteristics'),
            )
            return redirect('/products')
        else:
            return render(request, self.template_name, context=self.get_context_data(form=form))


class DetailProductView(CreateView, DetailView):
    template_name = 'products/detail.html'
    form_class = ReviewCreateForm
    model = Review

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'user': get_user_from_request(self.request),
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'product': kwargs['product'],
            'reviews': kwargs['reviews'],
            'categories': kwargs['categories']
        }

    def post(self, request, id, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                author_id=request.user.id,
                text=form.cleaned_data.get('text'),
                product_id=id,
                grade=form.cleaned_data.get('grade'),
            )
            return redirect(f'/products/{id}/')
        else:
            product = Product.objects.get(id=id)
            reviews = Review.objects.filter(product_id=id)
            categories = product.category.all()

            return render(request, self.template_name, context=self.get_context_data(
                form=form,
                product=product,
                reviews=reviews,
                categories=categories
            ))






































