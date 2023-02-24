import copy
import random

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from backend.website.base.models import Song, Playlist, Artist


@require_http_methods(['POST'])
def all_search(request):
    value = request.POST.get('value')  # The search term
    type = request.POST.get('type')  # The search criteria

    results = []

    match type.lower():
        case "song":
            template_name = 'search/partials/_song_results.html'
            songs = Song.objects.filter(name__icontains=value)

            for song in songs:
                result = {
                    "song": song.to_dict()
                }

                copied_result = copy.deepcopy(result)
                results.append(copied_result)

            context = {
                "results": results
            }

        case "artist":
            template_name = 'search/partials/_artist_results.html'
            artists = Artist.objects.filter(name__icontains=value)

            for artist in artists:
                result = {
                    "name": artist.name,
                    "number_of_songs": artist.song_set.all().count(),
                    "age": random.randint(20, 60),
                    "genre": "Pop"
                }

                copied_result = copy.deepcopy(result)
                results.append(copied_result)
            context = {
                "results": results
            }

        case "playlist":
            template_name = 'playlist/partials/all-playlists-page/_playlist_list.html'
            playlists = Playlist.objects.filter(name__icontains=value)
            context = {
                "playlists": playlists
            }

        case default:
            template_name = 'search/partials/_song_results.html'
            songs = Song.objects.filter(name__icontains=value)

            for song in songs:
                result = {
                    "name": song.name
                }

                copied_result = copy.deepcopy(result)
                results.append(copied_result)

            context = {
                "results": results
            }
    return render(request, template_name, context)
