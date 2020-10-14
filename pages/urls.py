
from django.urls import path

from pages.views import HomePageView, BlogPageView, CategoryPageView, ContactPageView, BasketPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('category', CategoryPageView.as_view(), name='category'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('basket', BasketPageView.as_view(), name='basket'),
]
