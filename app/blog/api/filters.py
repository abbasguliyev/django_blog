import django_filters

from blog.models import Blog, Category, Questions

class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'category': ['exact'],
            'author': ['exact'],
            'created_date': ['exact', 'gte', 'lte'],
        }

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact']
        }

class QuestionsFilter(django_filters.FilterSet):
    class Meta:
        model = Questions
        fields = {
            'owner' : ['exact'],
            'title': ['exact', 'icontains'],
            'subject': ['exact', 'icontains'],
        }