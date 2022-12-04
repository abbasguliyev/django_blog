import django_filters

from account.models import (
    UserWishList
)

class UserWishListFilter(django_filters.FilterSet):
    class Meta:
        model = UserWishList
        fields = {
            'user': ['exact'],
            'user__email': ['exact'],
            'user__id': ['exact'],
        }
