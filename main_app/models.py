from django.db import models
from django.forms import CharField

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),

)

LANGUAGE_CHOICES = (
    ('UZ', 'UZBEK'),
    ('RU', 'RUSSIAN'),

)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),

)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    view_count = models.IntegerField(default=0)
    rated = models.IntegerField(default=0)
    video_src = models.FileField(upload_to='video/%y')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.get_url()


class MyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Movie', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Movie', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Instagram(models.Model):
    username = CharField(max_length=255)

    def __str__(self):
        return self.username
