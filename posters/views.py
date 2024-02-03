from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Poster

def fetch_posters(request):
    """ A view to show all posters, including sorting and search queries """

    posters = Poster.objects.all()
    query = None

    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You did not enter any search criteria!")
                return redirect(reverse('posters'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            posters = posters.filter(queries)

            # Check for no matches
            if not posters:
                messages.error(request, "There are no posters that match the search criteria!")
                return redirect(reverse('posters'))

    context = {
        'posters': posters,
        'search_term': query,
    }

    return render(request, 'posters/posters.html', context)


def poster_details(request, poster_id):
    """ A view to show individual poster details """

    poster = get_object_or_404(Poster, pk=poster_id)

    context = {
        'poster': poster,
    }
    return render(request, 'posters/poster_details.html', context)
