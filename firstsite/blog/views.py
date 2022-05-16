from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'



def showpost(request):
    return HttpResponse('Post')

def showtag(request):
    return HttpResponse('Tags')
