from django.contrib import admin
from django.urls import path, include

from posts.views import post_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('',include('posts.urls')),
    path('',include('contact.urls')),
    path('',include('merch.urls')),
]