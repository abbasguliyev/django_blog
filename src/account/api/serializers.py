from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.models import UserWishList

User= get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class UserWishListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserWishList
        fields = "__all__"
