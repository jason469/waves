from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path, include

urlpatterns = [
    # Website configuration
    re_path(r'^static/(?P<path>.*)$', views.serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', views.serve, {'document_root': settings.MEDIA_ROOT}),

    # API
    path('api/', include('backend.api.urls')),

    # Website
    path('', include('backend.website.base.urls')),
    path('playlist/', include('backend.website.playlist.urls')),
    path('search/', include('backend.website.search.urls')),

    # Admin
    path('admin/', admin.site.urls),
]

