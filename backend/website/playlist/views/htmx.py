from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django_htmx.http import trigger_client_event

from backend.website.base.models import Playlist, PlaylistSong, Song
from backend.website.playlist.forms import AddPlaylistForm, UpdatePlaylistForm

@require_http_methods(['POST'])
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

    # playlists = Playlist.objects.filter(user=current_user)
    context = {
        "playlist": new_playlist,
    }
    return render(request, 'playlist/partials/common/_playlist_card.html', context=context)

    # return render(request, "playlist/partials/messages/_add_playlist_message.html", context)

@require_http_methods(['POST'])
def update_playlist(request):
    old_playlist_id = request.POST.get('oldPlaylistId')  # The name of the old playlist
    new_playlist_name = request.POST.get('name')  # The name of the new playlist
    new_description = request.POST.get('description')  # An optional description of the new playlist
    current_user = request.user

    form = UpdatePlaylistForm(request.POST)

    if form.is_valid():
        playlist_updated = True
        try:
            existing_playlist = Playlist.objects.get(
                id=old_playlist_id,
                user=current_user
            )
            existing_playlist.name = new_playlist_name
            existing_playlist.description = new_description
            existing_playlist.save()

        except Exception as exc:
            existing_playlist = Playlist.objects.none()
            print(exc)
    else:
        existing_playlist = Playlist.objects.none()
        playlist_updated = False

    print('existing playlist is', existing_playlist)
    context = {
        "playlist": existing_playlist,
        "playlist_updated": playlist_updated
    }

    response = render(request, 'playlist/partials/playlist-detail-page/playlist_identification.html', context=context)
    trigger_client_event(response, 'update_playlist', {})  # Will trigger a custom event called update_playlist

    return response


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
        response = HttpResponse()
        response["HX-Redirect"] = reverse('website__playlist:all-playlists')
        return response

    except Exception as exc:
        print(exc)

    return HttpResponse()


# This function will return the playlist's current name in a hidden input tag
@require_http_methods(['GET'])
def get_playlist_tag(request, playlist_id):
    current_user = request.user

    try:
        playlist = Playlist.objects.get(
            id=playlist_id,
            user=current_user
        )
    except Exception as exc:
        print(exc)
        playlist = Playlist.objects.none()

    context = {
        "playlist": playlist
    }

    return render(request, 'playlist/partials/common/_playlist_name_tag.html', context=context)

@require_http_methods(['POST'])
def add_to_playlist(request):
    print(request.POST)
    playlist_id = request.POST.get('all_playlists')
    song_id = request.POST.get('songId')

    try:
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)

        existing_playlistsong = PlaylistSong.objects.filter(
            playlist=playlist,
            song=song
        )

        if len(existing_playlistsong) == 0:
            PlaylistSong.objects.create(
                playlist=playlist,
                song=song
            )
        else:
            playlistSongExists = True
    except Exception as exc:
        print(exc)

    return HttpResponse('Add')

