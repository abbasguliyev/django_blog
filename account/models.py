from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserReadBlogs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="read_blogs")
    read_blogs = models.ManyToManyField("blog.Blog", blank=True, related_name="read_blogs")

class UserWishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name="wish_lists")
    wish_list = models.ManyToManyField("blog.Blog", blank=True, related_name="wish_lists")

