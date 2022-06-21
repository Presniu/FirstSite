from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("tags/", views.Tags.as_view(), name="tags"),
    path("tag/<slug:tag_slug>/", views.OneTag.as_view(), name="tag"),
    path("post/<int:post_id>", views.ShowPost.as_view(), name="post"),
    path("authors/", views.Authors.as_view(), name="authors"),
    path("posts/<int:page>/", views.Pages.as_view(), name="pages"),
    path("auth/", views.Auth.as_view(), name="auth"),
    path("registration/", views.Registration.as_view(), name="registration"),
    path("add/", views.AddArticle.as_view(), name="addarticle"),
    path("logout", views.logout, name="logout"),
]
