import copy

from django import template

from backend.website.playlist.forms import AddPlaylistForm, SelectPlaylistForm

register = template.Library()


@register.inclusion_tag('templatetags/playlist/_add_playlist.html')
def add_playlist():
    return {
        "add_playlist_form": AddPlaylistForm,
    }


@register.inclusion_tag('templatetags/playlist/_add_to_playlist.html', takes_context=True)
def add_to_playlist(context):
    request = context['request']
    return {
        "select_playlist_form": SelectPlaylistForm(request.user),
    }
