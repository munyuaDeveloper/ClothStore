
from django.urls import path

from pages.views import (
    HomePageView,
    ContactPageView,
)

urlpatterns = [
    path('', HomePageView, name='home'),
    path('contact', ContactPageView.as_view(), name='contact'),
]
