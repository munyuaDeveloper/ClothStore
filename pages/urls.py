
from django.urls import path

from pages.views import (
    HomePageView,
    BlogPageView,
    ContactPageView,
    PostDetailsPageView
)

urlpatterns = [
    path('', HomePageView, name='home'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('post-details', PostDetailsPageView.as_view(), name='post-details'),
]
