from django.urls import path, include

urlpatterns = [
    path('account/', include('api.v1.account.urls')),
    path('contact/', include('api.v1.contact.urls')),
    path('blog/', include('api.v1.blog.urls')),
]
