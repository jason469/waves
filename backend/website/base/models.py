from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    """
    Artists
    """
    name = models.CharField(max_length=255, blank=False, null=False, default='')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']


class Song(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'artist']

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "artist": self.artist.name
        }


class Playlist(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # Who created the playlist
    songs = models.ManyToManyField(Song, through='PlaylistSong')
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "username": self.user.username
        }

    class Meta:
        unique_together = ['name', 'user']



class PlaylistSong(models.Model):
    """
    This table shows which songs belong to which playlists
    """
    playlist = models.ForeignKey(Playlist, blank=True, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(Song, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Playlist - {self.playlist.name} and Song - {self.song.name}'

    class Meta:
        verbose_name = "PlaylistSong"
        verbose_name_plural = "PlaylistSongs"
