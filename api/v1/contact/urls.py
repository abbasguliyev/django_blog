from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactListCreateAPIView.as_view()),
    path('<int:pk>', views.ContactDetailAPIView.as_view()),
]
