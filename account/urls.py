from django.contrib import admin
from django.urls import path, include
from .views import SignUpView
urlpatterns = [
    path('register/', SignUpView.as_view(), name='register')
]
