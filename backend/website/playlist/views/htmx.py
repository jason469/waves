from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from backend.website.base.models import Playlist, PlaylistSong
from backend.website.playlist.forms import AddPlaylistForm


def add_playlist(request):
    playlist_name = request.POST.get('name')  # The name of the new playlist
    description = request.POST.get('description')  # An optional description of the new playlist
    current_user = request.user

    new_playlist = None

    form = AddPlaylistForm(request.POST)

    if form.is_valid():
        try:
            existing_playlist = Playlist.objects.get(
                name=playlist_name,
                user=current_user
            )
            playlist_created = False
            playlist_exist = True
        except Playlist.DoesNotExist:
            playlist_exist = False
            try:
                new_playlist = Playlist.objects.create(
                    name=playlist_name,
                    description=description,
                    user=current_user
                )
                playlist_created = True
            except Exception as exc:
                playlist_created = False
    else:
        playlist_created = False
        playlist_exist = False

    # context = {
    #     "playlist_created": playlist_created,
    #     "playlist_exist": playlist_exist,
    #     "new_playlist": new_playlist
    # }

    playlists = Playlist.objects.filter(user=current_user)
    context = {
        "playlists": playlists,
    }
    return render(request, 'playlist/partials/_playlist_list.html', context=context)


    # return render(request, "playlist/partials/messages/_add_playlist_message.html", context)


@require_http_methods(['DELETE'])
def delete_playlist(request, playlist_name):
    current_user = request.user

    try:
        # Find the playlist and songs within the playlist
        playlist = Playlist.objects.get(
            name=playlist_name,
            user=current_user
        )
        playlist_songs = PlaylistSong.objects.filter(
            playlist=playlist
        )

        # Delete the playlist and all songs in the playlist
        for playlist_song in playlist_songs:
            playlist_song.delete()
        playlist.delete()

    except Exception as exc:
        print(exc)

    return HttpResponse()

