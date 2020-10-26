from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from products.models import Product


def HomePageView(request):
    products = Product.objects.filter(available=True)[:10]
    product_count_cat = products.count()
    context = {
        'products': products,
        'product_count_cat': product_count_cat}
    return render(request, 'index.html', context)


class BlogPageView(TemplateView):
    template_name = 'blog.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class PostDetailsPageView(TemplateView):
    template_name = 'post.html'
