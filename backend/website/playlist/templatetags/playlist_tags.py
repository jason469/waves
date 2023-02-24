import copy

from django import template

from backend.website.base.models import Playlist, Song
from backend.website.playlist.forms import AddPlaylistForm, SelectPlaylistForm

register = template.Library()


@register.inclusion_tag('templatetags/playlist/_add_playlist.html')
def add_playlist():
    return {
        "add_playlist_form": AddPlaylistForm,
    }


@register.inclusion_tag('templatetags/playlist/_add_to_playlist.html', takes_context=True)
def add_to_playlist(context, song_id):
    request = context['request']
    song_name = Song.objects.get(id=song_id).name
    return {
        "select_playlist_form": SelectPlaylistForm(request.user),
        "song_id": song_id,
        "song_name": song_name
    }

@register.inclusion_tag('templatetags/playlist/_navbar__all_playlists.html', takes_context=True)
def navbar_all_playlists(context):
    request = context['request']
    all_playlists = Playlist.objects.filter(
        user=request.user
    )
    return {
        "all_playlists": all_playlists,
    }
