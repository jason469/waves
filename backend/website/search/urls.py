from django.contrib.auth.decorators import login_required
from django.urls import path

from backend.website.search.views import views, htmx

app_name = 'website__search'

urlpatterns = [
    path('', login_required(views.search), name='search'),
]

htmx_urlpatterns = [
    path('htmx-all-search', login_required(htmx.all_search), name='htmx-all-search'),
]

urlpatterns += htmx_urlpatterns
