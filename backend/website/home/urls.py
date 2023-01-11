from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from backend.website.home.views import *

app_name = 'website__home'
urlpatterns = [
    # --------------- Main/misc. page URLs ---------------#
    path('', login_required(index), name='index'),

]