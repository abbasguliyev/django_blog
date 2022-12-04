from rest_framework import status, generics
from rest_framework.response import Response
from blog.models import Blog, Category
from api.v1.blog.serializers import BlogSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from api.v1.blog import filters
from rest_framework import pagination
from main.permissions import IsAdminUserOrReadOnly

User = get_user_model()

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.BlogFilter
    pagination.LimitOffsetPagination.page_size = 3 
    permission_classes = (IsAdminUserOrReadOnly, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            author = request.user
            serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAdminUserOrReadOnly, )

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


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.CategoryFilter
    permission_classes = (IsAdminUserOrReadOnly, )

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly, )

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