from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Теги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reversed('post', kwargs={'post_slug': self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('tags', kwargs={'tag_slug': self.slug})
