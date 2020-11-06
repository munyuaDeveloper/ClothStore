from django.urls import path

from posts.views import blog, post

# app_name = 'posts'
urlpatterns = [
    path('', blog, name='post_list'),
    path('post/<id>', post, name='post_details'),
]
