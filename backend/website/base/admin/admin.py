from django.contrib import admin

from backend.website.base.admin.forms import PlaylistAdminForm, SongAdminForm, ArtistAdminForm
from backend.website.base.models import Playlist, Song, PlaylistSong, Artist


# Readonly permission for an admin table
# def has_delete_permission(self, request, obj=None):
#     return False
#
#
# def has_add_permission(self, request, obj=None):
#     return False
#
#
# def has_change_permission(self, request, obj=None):
#     return False


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    search_fields = ["name", "user__username"]
    list_filter = ["user__username"]

    form = PlaylistAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('name', "user",)
        }),
        ('Parameters', {
            'fields': ("description",)
        }),
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

    form = SongAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('name', 'artist')
        }),
    )


@admin.register(PlaylistSong)
class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ["playlist", "song"]
    search_fields = ["playlist__name"]

    form = SongAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('playlist', "song",)
        }),
    )


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

    form = ArtistAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('name',)
        }),
    )
