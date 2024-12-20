from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="blogs")
    image = models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")

    def __str__(self) -> str:
        return self.title

class Questions(models.Model):
    title = models.CharField(max_length=500)
    subject = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")

    def __str__(self) -> str:
        return self.title