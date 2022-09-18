import django_filters

from account.models import (
    UserReadBlogs,
    UserWishList
)

class UserReadBlogsFilter(django_filters.FilterSet):
    class Meta:
        model = UserReadBlogs
        fields = {
            'user': ['exact'],
            'user__email': ['exact'],
            'user__id': ['exact'],
        }

class UserWishListFilter(django_filters.FilterSet):
    class Meta:
        model = UserWishList
        fields = {
            'user': ['exact'],
            'user__email': ['exact'],
            'user__id': ['exact'],
        }
