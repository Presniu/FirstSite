import datetime

from django.contrib.auth import login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import AddArticleForm, AuthenticationForm, RegisterUserForm
from .models import Post, Tag
from .utils import DataMixin


class Home(DataMixin, ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-time_create"]

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        extra = self.get_post_content(title="Блог")
        return dict(list(content.items()) + list(extra.items()))


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_context_data(self, **kwargs):
        content = super().get_context_data()
        extra = self.get_post_content(title=self.object.title)
        return dict(list(content.items()) + list(extra.items()))


class Authors(DataMixin, ListView):
    model = Post
    template_name = "blog/authors.html"
    context_object_name = "posts"

    def get_queryset(self):
        return (
            Post.objects.values("author")
            .annotate(count=Count("author"))
            .order_by("author")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        extra = self.get_post_content(title="Автора")
        return dict(list(content.items()) + list(extra.items()))


class Pages(DataMixin, ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        extra = self.get_post_content(title=f'Post page #{self.kwargs["page"]}')
        return dict(list(content.items()) + list(extra.items()))


class OneTag(DataMixin, ListView):
    model = Post
    template_name = "blog/tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["tag_slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        extra = self.get_post_content(
            title=Tag.objects.get(slug=self.kwargs["tag_slug"]).name,
        )
        return dict(list(content.items()) + list(extra.items()))


class Tags(DataMixin, ListView):
    model = Tag
    template_name = "blog/tags.html"
    context_object_name = "posts"
    ordering = "name"

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(Tags, self).get_context_data(**kwargs)
        extra = self.get_post_content(title="Теги")
        return dict(list(content.items()) + list(extra.items()))


class Auth(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = "blog/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra = self.get_post_content(title="Авторизация")
        return dict(list(context.items()) + list(extra.items()))

    def get_success_url(self):
        return reverse_lazy("home")


class Registration(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("auth")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra = self.get_post_content(title="Регистрация")
        return dict(list(context.items()) + list(extra.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class AddArticle(DataMixin, FormView):
    template_name = "blog/newarticle.html"
    form_class = AddArticleForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra = self.get_post_content(title="Добавление статьи")
        return dict(list(context.items()) + list(extra.items()))

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        text = form.cleaned_data["text"]
        if "photo" in form.cleaned_data:
            photo = form.cleaned_data["photo"]
        else:
            photo = None
        tags = form.cleaned_data["tags"]
        time_create = datetime.datetime.now()
        author = self.request.user.username
        form_data = Post(title=title, text=text, time_create=time_create, author=author)
        form_data.save()
        if photo:
            form_data.photo = photo
        for tag in tags:
            form_data.tags.add(tag)
        form_data.save()
        return redirect("home")


def logout(request):
    dj_logout(request)
    return redirect("home")
