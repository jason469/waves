from django import forms
from django.contrib.auth.models import User

from backend.config.utils import create_request_object
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

        widgets = {
            'description': forms.Textarea(
                attrs={'placeholder': 'Add an optional description'}),
        }


class SelectPlaylistForm(forms.Form):
    required_css_class = 'required'

    all_playlists = forms.ModelChoiceField(
        queryset=None,
        help_text="Select the playlist you want to add",
    )

    def __init__(self, user, *args, **kwargs):
        super(SelectPlaylistForm, self).__init__(*args, **kwargs)
        self.fields['all_playlists'].queryset = Playlist.objects.filter(user=user).order_by('name')
