from django import forms


class PlaylistAdminForm(forms.ModelForm):
    class Meta:
        help_texts = {
            'name': 'Name of the playlist',
            'user': 'Owner of the playlist',
        }


class SongAdminForm(forms.ModelForm):
    class Meta:
        help_texts = {
            'name': 'Name of the song',
        }


class PlaylistSongAdminForm(forms.ModelForm):
    class Meta:
        help_texts = {
            'song': 'Song',
            'playlist': 'Playlist',
        }


class ArtistAdminForm(forms.ModelForm):
    class Meta:
        help_texts = {
            'name': 'Name of the artist',
            'songs': 'What songs has this artist done',
        }
