from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView

urlpatterns = [
    path('v1/products/categories', CategoryListView.as_view(), name="category_list"),
    path('v1/products', ProductListView.as_view(), name="product_list"),
    path('v1/products/detail', ProductDetailView.as_view(), name="product_details")
]
