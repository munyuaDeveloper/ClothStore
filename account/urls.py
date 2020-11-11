from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, MyAccount, OrderDetails

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('my-account/', MyAccount, name='my-account'),
    path('my-account/order/<id>', OrderDetails, name='order_details')
]
