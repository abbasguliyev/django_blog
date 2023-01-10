from account.api.selectors import user_list, user_wish_list_list
from account.models import UserWishList
from django.contrib.auth import get_user_model
User = get_user_model()

def create_user(*, email: str, username: str, password: str) -> User:
    obj = User.objects.create_user(email=email, username=username, password=password)
    obj.full_clean()
    return obj

def update_user(instance, **data) -> User:
    obj = user_list().filter(pk=instance.id).update(**data)
    return obj

def create_user_wish_list(*, user, wish_list) -> UserWishList:
    user_wish_list = user_wish_list_list().filter(user=user)
    if user_wish_list.count() == 0:
        user_wish_list = UserWishList.objects.create(user=user)
        for w in wish_list:
            user_wish_list.wish_list.add(w)
            user_wish_list.save()
    else:
        for w in wish_list:
            user_wish_list.last().wish_list.add(w)
            user_wish_list.last().save()

    return user_wish_list

def update_user_wish_list(instance, **data) -> UserWishList:
    obj = user_wish_list_list().filter(pk=instance.id).update(**data)
    return obj
