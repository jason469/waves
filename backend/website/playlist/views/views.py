from django.shortcuts import render

from backend.website.base.models import Playlist, Song
from backend.website.playlist.forms import AddPlaylistForm


def all_playlists(request):
    user = request.user

    playlists = Playlist.objects.filter(user=user)
    context = {
        "add_playlist_form": AddPlaylistForm,
        "playlists": playlists
    }
    return render(request, 'playlist/pages/all-playlists.html', context=context)


def playlist_detail(request, name):
    user = request.user

    try:
        playlist = Playlist.objects.get(
            user=user,
            name=name
        )
        songs = playlist.songs.all()
    except Exception as exc:
        print(exc)
        playlist = Playlist.objects.none()
        songs = Song.objects.none()

    context = {
        "playlist": playlist,
        "songs": songs
    }
    return render(request, 'playlist/pages/playlist-detail.html', context=context)

