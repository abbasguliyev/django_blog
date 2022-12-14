from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListCreateAPIView.as_view()),
    path('<int:pk>/', views.BlogDetailAPIView.as_view()),

    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view()),

    path('questions/', views.QuestionsListCreateAPIView.as_view()),
    path('questions/<int:pk>/', views.QuestionsDetailAPIView.as_view()),
]
