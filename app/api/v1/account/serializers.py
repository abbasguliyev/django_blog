from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.models import UserWishList

User= get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'], 
            last_name=validated_data['last_name'], 
            email=validated_data['email'], 
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username')


class UserWishListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserWishList
        fields = "__all__"
