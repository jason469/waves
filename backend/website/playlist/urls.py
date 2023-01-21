from django.contrib.auth.decorators import login_required
from django.urls import path

from backend.website.playlist.views import views, htmx

app_name = 'website__playlist'

urlpatterns = [
    path('', login_required(views.all_playlists), name='all-playlists'),
    path('<str:name>/', login_required(views.playlist_detail), name='playlist-detail'),
]

htmx_urlpatterns = [
    path('htmx-add-playlist', login_required(htmx.add_playlist), name='htmx-add-playlist'),
    path('htmx-delete-playlist/<str:playlist_name>', login_required(htmx.delete_playlist), name='htmx-delete-playlist'),
]

urlpatterns += htmx_urlpatterns
