from rest_framework import status, generics, permissions
from rest_framework.response import Response
from blog.models import Blog, Category, Questions
from blog.api.serializers import BlogSerializer, CategorySerializer, QuestionsSerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from blog.api import filters, selectors, services
from main.permissions import IsAdminUserOrReadOnly
from main.permissions import IsOwner
User = get_user_model()

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = selectors.blog_list()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.BlogFilter
    permission_classes = (IsAdminUserOrReadOnly, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        services.create_blog(user=user, **serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selectors.blog_list()
    serializer_class = BlogSerializer
    permission_classes = (IsAdminUserOrReadOnly, )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        services.update_blog(instance=instance, **serializer.validated_data)
        return Response(serializer.data)

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = selectors.category_list()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.CategoryFilter
    permission_classes = (IsAdminUserOrReadOnly, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_category(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selectors.category_list()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly, )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        services.update_category(instance=instance, **serializer.validated_data)
        return Response(serializer.data)

class QuestionsListCreateAPIView(generics.ListCreateAPIView):
    queryset = selectors.questions_list()
    serializer_class = QuestionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.QuestionsFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        services.create_question(user=user, **serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class QuestionsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selectors.questions_list()
    serializer_class = QuestionsSerializer
    permission_classes = [IsOwner,]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        services.update_question(instance=instance, **serializer.validated_data)
        return Response(serializer.data)