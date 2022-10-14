from django.contrib.auth import user_logged_in
from rest_framework import status, generics
from rest_framework.response import Response

from account.models import UserReadBlogs, UserWishList
from . import jwt as custom_jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, UserReadBlogsSerializer, UserSerializer, UserWishListSerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from api.v1.account import filters
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class CurrentUser(APIView):
    def get(self, request):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        except:
            return Response({"detail": "Login olmamısınız"}, status=status.HTTP_400_BAD_REQUEST)
        


class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = custom_jwt.jwt_decode_handler(data.get("access"))

        if not User.objects.filter(id=acces_token.get("user_id")).last():
            return Response({"error": True, "message": "No such a user"}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.filter(id=acces_token.get("user_id")).last()
        user_logged_in.send(sender=type(user), request=request, user=user)

        user_details = UserSerializer(user)

        data["user_details"] = user_details.data
        return Response(data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class UserReadBlogsListAPIView(generics.ListAPIView):
    queryset = UserReadBlogs.objects.all()
    serializer_class = UserReadBlogsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.UserReadBlogsFilter

class UserReadBlogsDetailAPIView(generics.RetrieveAPIView):
    queryset = UserReadBlogs.objects.all()
    serializer_class = UserReadBlogsSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class UserWishListListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserWishList.objects.all()
    serializer_class = UserWishListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.UserWishListFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            wish_list = serializer.validated_data.get('wish_list')
            print(f"{wish_list=}")
            user_wish_list = UserWishList.objects.filter(user=user)
            if len(user_wish_list) == 0:
                user_wish_list = UserWishList.objects.create(user=user)
                for w in wish_list:
                    user_wish_list[0].wish_list.add(w)
                    user_wish_list[0].save()
            else:
                for w in wish_list:
                    user_wish_list[0].wish_list.add(w)
                    user_wish_list[0].save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserWishListDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserWishList.objects.all()
    serializer_class = UserWishListSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
