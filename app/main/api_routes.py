from django.urls import path, include

urlpatterns = [
    path('account/', include('account.api.urls')),
    path('contact/', include('contact.api.urls')),
    path('blog/', include('blog.api.urls')),
]
