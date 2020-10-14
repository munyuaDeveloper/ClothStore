from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class BlogPageView(TemplateView):
    template_name = 'blog.html'


class CategoryPageView(TemplateView):
    template_name = 'category.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class BasketPageView(TemplateView):
    template_name = 'basket.html'
