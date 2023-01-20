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
            'playlists': 'List of playlists the song is in',
        }


class PlaylistSongAdminForm(forms.ModelForm):
    class Meta:
        help_texts = {
            'song': 'Song',
            'playlist': 'Playlist',
        }
