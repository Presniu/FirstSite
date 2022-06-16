from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tags/', Tags.as_view(), name='tags'),
    path('tag/<slug:tag_slug>/', OneTag.as_view(), name='tag'),
    path('post', showpost, name='post'),
    path('authors/', Authors.as_view(), name='authors'),
    path('posts/<int:page>/', Pages.as_view(), name='pages'),
    path('auth/', Auth.as_view(), name='auth'),
    path('registration/', Registration.as_view(), name='registration'),
    path('add/', addarticle, name='addarticle'),
    path('logout', logout, name='logout')
]