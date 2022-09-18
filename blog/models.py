from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    body = RichTextField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="blogs")
    image = models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self) -> str:
        return self.title