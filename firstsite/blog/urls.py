from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tags/', showtag, name='tag'),
    path('post', showpost, name='post')

]