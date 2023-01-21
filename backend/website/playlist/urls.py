from django.contrib.auth.decorators import login_required
from django.urls import path

from backend.website.playlist.views import views, htmx

app_name = 'website__playlist'

urlpatterns = [
    path('', login_required(views.all_playlists), name='all-playlists'),
]

htmx_urlpatterns = [
    path('htmx-add-playlist', login_required(htmx.add_playlist), name='htmx-add-playlist'),
]

urlpatterns += htmx_urlpatterns
