from django.shortcuts import render

from backend.website.search.forms import AllSearchForm


def search(request):
    context = {
        "search_form": AllSearchForm
    }
    return render(request, 'search/pages/search.html', context=context)
