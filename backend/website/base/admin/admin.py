from django.contrib import admin

from backend.website.base.admin.forms import PlaylistAdminForm, SongAdminForm, ArtistAdminForm, PlaylistSongAdminForm
from backend.website.base.models import Playlist, Song, PlaylistSong, Artist


# Readonly permission for an admin table
def has_delete_permission(self, request, obj=None):
    return False


def has_add_permission(self, request, obj=None):
    return False


def has_change_permission(self, request, obj=None):
    return False


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["name", "get_artist_name", "get_playlists_name"]
    search_fields = ["name", "artist__name"]
    list_filter = ["artist__name"]

    form = SongAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('name', 'artist')
        }),
    )

    def get_artist_name(self, obj):
        return obj.artist.name

    def get_playlists_name(self, obj):
        return f", \n".join([playlistsong.playlist.name for playlistsong in obj.playlistsong_set.all()])

    get_artist_name.short_description = "Artist"
    get_playlists_name.short_description = "Playlist names"


class SongInline(admin.TabularInline):
    model = Song
    extra = 0
    form = SongAdminForm


@admin.register(PlaylistSong)
class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ["playlist", "song"]
    search_fields = ["playlist__name", "song__name"]
    list_filter = ["playlist__name"]

    form = PlaylistSongAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('playlist', "song",)
        }),
    )


class PlaylistSongInline(admin.TabularInline):
    model = PlaylistSong
    extra = 0
    form = PlaylistSongAdminForm


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "get_songs"]
    search_fields = ["name"]
    inlines = [SongInline]

    form = ArtistAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('name',)
        }),
    )

    def get_songs(self, obj):
        return f", \n".join([song.name for song in obj.song_set.all()])

    get_songs.short_description = "Songs"


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "get_number_of_songs", 'date_created']
    search_fields = ["name", "user__username"]
    list_filter = ["user__username"]
    inlines = [PlaylistSongInline]

    form = PlaylistAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('name', "user",)
        }),
        ('Parameters', {
            'fields': ("description",)
        }),
    )

    def get_number_of_songs(self, obj):
        return obj.songs.all().count()

    get_number_of_songs.short_description = "Number of Songs"
