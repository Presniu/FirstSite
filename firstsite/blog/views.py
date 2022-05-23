from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     content = super().get_context_data(**kwargs)
    #     extra = self.get_post_content(title='Main page')
    #     return dict(list(content.items()) + list(extra.items()))

def showpost(request):
    return HttpResponse('Post')

def showtag(request):
    return HttpResponse('Tags')
