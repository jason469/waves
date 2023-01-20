from django.contrib.auth.decorators import login_required
from django.urls import path

from backend.website.search.views import views, htmx

app_name = 'website__search'

urlpatterns = [
    path('', login_required(views.all_search), name='all-search'),
]

htmx_urlpatterns = [
]

urlpatterns += htmx_urlpatterns
