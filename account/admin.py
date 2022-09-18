from django.contrib import admin
from .models import User, UserReadBlogs, UserWishList
# Register your models here.

admin.site.register(User)
admin.site.register(UserReadBlogs)
admin.site.register(UserWishList)