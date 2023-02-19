from django.db.models.query import QuerySet
from blog.models import Blog, Category, Questions

def blog_list() -> QuerySet[Blog]:
    qs = Blog.objects.select_related('category', 'author').all()
    return qs

def category_list() -> QuerySet[Category]:
    qs = Category.objects.all()
    return qs

def questions_list() -> QuerySet[Questions]:
    qs = Questions.objects.select_related('owner').all()
    return qs