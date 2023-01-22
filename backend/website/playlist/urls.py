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
    path('htmx-add-to-playlist', login_required(htmx.add_to_playlist), name='htmx-add-to-playlist'),
    path('htmx-update-playlist', login_required(htmx.update_playlist), name='htmx-update-playlist'),
    path('htmx-delete-playlist/<str:playlist_name>', login_required(htmx.delete_playlist), name='htmx-delete-playlist'),
    path('htmx-get-playlist-tag/<int:playlist_id>', login_required(htmx.get_playlist_tag), name='htmx-get-playlist-tag'),


]

urlpatterns += htmx_urlpatterns
