from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')

    def __str__(self):
        return f'Tag - {self.name}'

    class Meta:
        ordering = ['name']
        unique_together = ['name']


class Playlist(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Playlist - {self.name}'

    class Meta:
        unique_together = ['name', 'user']


class Song(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='')
    tags = models.ManyToManyField(Tag, through='TagSong')
    playlists = models.ManyToManyField(Playlist, through='PlaylistSong')

    def __str__(self):
        return f'Song - {self.name}'

    class Meta:
        ordering = ['name']


class TagSong(models.Model):
    tag = models.ForeignKey(Tag, blank=True, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(Song, blank=True, on_delete=models.DO_NOTHING)


class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, blank=True, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(Song, blank=True, on_delete=models.DO_NOTHING)
