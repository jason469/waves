from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Playlist - {self.name}'

    class Meta:
        unique_together = ['name', 'user']


class Song(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    playlists = models.ManyToManyField(Playlist, through='PlaylistSong')

    def __str__(self):
        return f'Song - {self.name}'

    class Meta:
        ordering = ['name']


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
