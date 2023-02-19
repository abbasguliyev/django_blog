from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model
from account.models import UserWishList

User = get_user_model()

def user_list() -> QuerySet[User]:
    qs = User.objects.all()
    return qs

def user_wish_list_list() -> QuerySet[UserWishList]:
    qs = UserWishList.objects.select_related('user').prefetch_related('wish_list').all()
    return qs