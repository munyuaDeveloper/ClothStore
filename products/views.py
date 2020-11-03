from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from cart.forms import CartAddProductForm
from products.models import Category, SubCategory, Product


class CategoryPageView(ListView):
    model = Category
    template_name = 'category.html'


def product_list(request, category_slug=None, subcategory_slug=None, ):
    category = None
    subcategory = None
    product_count_cat = 0
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product_count_cat = products.count()
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        product_count_cat = products.count()
    if subcategory_slug:
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        products = products.filter(subcategory=subcategory)
    context = {'category': category,
               'categories': categories,
               'subcategory': subcategory,
               'products': products,
               'cart_product_form': cart_product_form,
               'product_count_cat': product_count_cat}
    return render(request,
                  'category.html',
                  context
                  )


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    similar_products = Product.objects.filter(category=product.category)
    product_count_cat = Product.objects.filter(category=product.category).count()
    categories = Category.objects.all()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'similar_products': similar_products,
                   'categories': categories,
                   'product_count_cat': product_count_cat})


class BasketPageView(TemplateView):
    template_name = 'basket.html'


class CheckoutPageView(TemplateView):
    template_name = 'checkout1.html'


class ItemDetailsPageView(TemplateView):
    template_name = 'detail.html'
