from django.shortcuts import render

from backend.website.base.models import Playlist
from backend.website.playlist.forms import AddPlaylistForm


def all_playlists(request):
    user = request.user

    playlists = Playlist.objects.filter(user=user)
    context = {
        "add_playlist_form": AddPlaylistForm,
        "playlists": playlists
    }
    return render(request, 'playlist/pages/all-playlists.html', context=context)
