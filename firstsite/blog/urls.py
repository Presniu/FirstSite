from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tags/', Tags.as_view(), name='tags'),
    path('post', showpost, name='post'),
    path('authors/', Authors.as_view(), name='authors'),
    path('posts/<int:page>/', Pages.as_view(), name='pages')
]