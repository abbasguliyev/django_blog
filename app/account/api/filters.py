import django_filters

from account.models import (
    UserWishList,
    User
)


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'is_superuser': ['exact']
        }

class UserWishListFilter(django_filters.FilterSet):
    class Meta:
        model = UserWishList
        fields = {
            'user': ['exact'],
            'user__email': ['exact'],
            'user__id': ['exact'],
        }
