from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.conf import settings


class CustomUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True, upload_to="images/users/%Y/%m")


class Category(models.Model):
    name = models.CharField(max_length=255, default="coding")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    insta_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=False)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article_detail', args=str(self.id))
        return reverse('home')
