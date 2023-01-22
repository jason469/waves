from django import forms

from backend.website.base.models import Playlist


class AddPlaylistForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Playlist
        exclude = ['user', 'songs']

        help_texts = {
            'name': 'Name of the playlist',
            'description': 'Description of the playlist',
        }


class UpdatePlaylistForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Playlist
        exclude = ['user', 'songs']

        help_texts = {
            'name': 'Name of the playlist',
            'description': 'Description of the playlist',
        }
