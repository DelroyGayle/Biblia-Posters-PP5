from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Poster, Category


def handle_sorting(request, the_sort_direction, posters):
    """ Handle the logic regarding the sorting of posters"""

    # 1) Determine the type of sort
    the_sort_key = request.GET['sort']
    the_sort_type = the_sort_key
    if the_sort_key == 'name':
        """
        For case insensitive 'name' searches
        Use 'lower_name' as the value of 'the_sort_key'
        Create an annotate field called 'lower_name' which holds
        the value of the name field in lowercase
        """
        the_sort_key = 'lower_name'
        posters = posters.annotate(lower_name=Lower('name'))

    # If category sort type has been selected, effectively perform
    # posters.order_by(category__name)
    if the_sort_key == 'category':
        the_sort_key = 'category__name'

    # 2) Determine the direction of the sort whether ascending or descending
    if 'direction' in request.GET:
        the_sort_direction = request.GET['direction']
        if the_sort_direction == 'desc':
            # Make the sort direction: Descending
            the_sort_key = f'-{the_sort_key}'

    # 3) Perform the Sort
    posters = posters.order_by(the_sort_key)
    return (the_sort_type, the_sort_direction, posters)


def fetch_posters(request):
    """
    A view to show all posters, including
    categorising, sorting and search queries
    """

    # Retrieve all the available posters
    posters = Poster.objects.all()

    # Reset all parameters to None
    query = None
    categories = None
    the_sort_type = None
    the_sort_direction = None

    if request.GET:
        # Nonnull request.GET
        if 'sort' in request.GET:
            # 1) Handle sorting
            (the_sort_type, the_sort_direction,
                posters) = handle_sorting(request, the_sort_direction,
                                          posters)

        # 2) Filter in regard to the selected category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posters = posters.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # 3) Filter in regard to the selected search query
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                # Null entry
                messages.error(request,
                               "You did not enter any search criteria!")
                return redirect(reverse('posters'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            posters = posters.filter(queries)

            # Check for no match
            if not posters:
                messages.error(request, ("There are no posters that match "
                                         "the search criteria!"))
                return redirect(reverse('posters'))

    current_sorting = f'{the_sort_type}_{the_sort_direction}'

    context = {
        'posters': posters,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'posters/posters.html', context)


def poster_details(request, poster_id):
    """ A view to show individual poster details """

    poster = get_object_or_404(Poster, pk=poster_id)

    context = {
        'poster': poster,
    }
    return render(request, 'posters/poster_details.html', context)
