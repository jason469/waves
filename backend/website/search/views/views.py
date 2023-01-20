from django.shortcuts import render


def all_search(request):
    context = {}
    return render(request, 'search/pages/all-search.html', context=context)
