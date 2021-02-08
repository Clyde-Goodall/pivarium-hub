from django.contrib import admin
from django.urls import path, include

#vestigial urls file, consider deleting
urlpatterns = [
    path('admin/', admin.site.urls)
]
