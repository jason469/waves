from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path, include

urlpatterns = [
    # Website configuration
    re_path(r'^static/(?P<path>.*)$', views.serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', views.serve, {'document_root': settings.MEDIA_ROOT}),
    # path('api/', include('website__home.urls', namespace='website__home')),
    # path('website/', include('website__home.urls', namespace='website__home')),

    # Apps
    path('admin/', admin.site.urls),
]

