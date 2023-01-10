from django.contrib.auth import user_logged_in
from rest_framework import status, generics
from rest_framework.response import Response

from account.api import jwt as custom_jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from account.api.serializers import RegisterSerializer, UserSerializer, UserWishListSerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from account.api import filters, services, selectors
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from main.permissions import IsOwnerUser

class RegisterApi(generics.CreateAPIView):
    queryset = selectors.user_list()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_user(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserList(generics.ListAPIView):
    queryset = selectors.user_list()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.UserFilter


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = selectors.user_list()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        services.update_user(instance=instance, **serializer.validated_data)
        return Response(serializer.data)

class UserDestroy(generics.DestroyAPIView):
    queryset = selectors.user_list().filter(is_superuser=False)
    serializer_class = UserSerializer

class CurrentUser(APIView):
    def get(self, request):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        except:
            return Response({"detail": "Login olmamısınız"}, status=status.HTTP_400_BAD_REQUEST)
        
class Login(TokenObtainPairView):
    permission_classes = [AllowAny,]
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = custom_jwt.jwt_decode_handler(data.get("access"))

        if not selectors.user_list().filter(id=acces_token.get("user_id")).last():
            return Response({"error": True, "message": "No such a user"}, status=status.HTTP_404_NOT_FOUND)

        user = selectors.user_list().filter(id=acces_token.get("user_id")).last()
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

class UserWishListListCreateAPIView(generics.ListCreateAPIView):
    queryset = selectors.user_wish_list_list()
    serializer_class = UserWishListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.UserWishListFilter
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        services.create_user_wish_list(user=user, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserWishListDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selectors.user_wish_list_list()
    serializer_class = UserWishListSerializer
    permission_classes = [IsOwnerUser,]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        services.update_user_wish_list(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
