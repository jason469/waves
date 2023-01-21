from django.shortcuts import render


def all_playlists(request):
    context = {}
    return render(request, 'playlist/pages/all-playlists.html', context=context)
