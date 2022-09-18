from django.urls import path
from . import views
from rest_framework_simplejwt.views import token_refresh

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('me/', views.CurrentUser.as_view()),
    path('register/', views.RegisterApi.as_view()),
    path("login/", views.Login.as_view()),
    path("token-refresh/", token_refresh),
    path('logout/', views.LogoutView.as_view()),

    path('read-blogs/', views.UserReadBlogsListAPIView.as_view()),
    path('read-blogs/<int:pk>', views.UserReadBlogsDetailAPIView.as_view()),

    path('wish-list/', views.UserWishListListCreateAPIView.as_view()),
    path('wish-list/<int:pk>', views.UserWishListDetailAPIView.as_view()),
]
