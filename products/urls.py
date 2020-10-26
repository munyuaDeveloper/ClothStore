from django.urls import path

from . import views
urlpatterns = [
    path('', views.product_list, name='category'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<slug:category_slug>/<slug:subcategory_slug>/', views.product_list,
         name='product_list_by_category_and_subcategory'),
    path('details/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('basket', views.BasketPageView.as_view(), name='basket'),
    path('checkout', views.CheckoutPageView.as_view(), name='checkout'),
    path('item-details', views.ItemDetailsPageView.as_view(), name='item-details'),
]
