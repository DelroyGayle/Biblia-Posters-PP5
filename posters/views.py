from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from bag.context_processors import checkfor_special_days

from biblia.common import Common

from .models import Poster, Category
from reviews.models import Review
from checkout.models import UserPurchasedPosters
from wishlist.models import Wishlist

from .forms import PosterForm


def reset_session_variables(request):
    """
    Ensure these variables are reset at this stage
    To avoiding page rendering issues
    """
    request.session.pop('backto_myreviews', None)
    request.session.pop('current_redirect_path', None)
    request.session.pop('purchased_posters', None)


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
        
    # Check if today is a Special Day
    if not Common.today_checked:
        checkfor_special_days(request)

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

    # Check if today is a Special Day
    if not Common.today_checked:
        checkfor_special_days(request)

    poster = get_object_or_404(Poster, pk=poster_id)
    poster_reviews = list(
        Review.objects.filter(poster=poster_id)
              .order_by('-amended_at').values()
    )

    (
        add_review_possible,
        update_review_possible,
        review_id,
        reviews
    ) = preprocess_reviews(poster_reviews, request, poster, poster_id)

    # Display wishlist option if user has registered
    add_to_wishlist = False
    if request.user.is_authenticated:
        # Add to wishlist or Remove from wishlist?
        add_to_wishlist = not (Wishlist.objects.filter(user=request.user.id,
                               poster=poster_id)
                                       .exists()
                               )

    context = {
        'poster': poster,
        'poster_reviews': poster_reviews,
        'add_review_possible': add_review_possible,
        'update_review_possible': update_review_possible,
        'review_id': review_id,
        'add_to_wishlist': add_to_wishlist,
    }
    request.session['poster_id'] = poster_id
    request.session['current_redirect_path'] = request.get_full_path()
    return render(request, 'posters/poster_details.html', context)


def preprocess_reviews(reviews, request, theposter, theposter_id):
    """
    Handles review's editing options
    and how reviews are display on the Poster Details Page

    1) If the user is NOT logged in then
    NO reviews editing options are shown at all

    Otherwise if the user is logged in
    2) Has the user purchased the poster in question?
    If NO,
        NO reviews editing options are shown at all

    If YES,
    3) Has the user already written a review for this poster?
        if NO,
            Display the 'Review - Add' option
        else

    4)
         Reorder the list so that the user's review APPEARS FIRST.
         Display the 'Review - Edit|Delete' option

    5) Format the Amend On Date and use this as the Review Date
    6) Create the HTML to display golden ratings stars
    """

    add_review_possible = False
    update_review_possible = False
    review_id = False
    review_index = -1
    theposter_id = int(theposter_id)

    if reviews:
        # Preprocess regarding dates and ratings
        for i in range(len(reviews)):
            # Format the review date
            reviews[i]['amended_at'] = (reviews[i]['amended_at']
                                        .strftime('%d %B %Y'))
            rating = reviews[i]['rating']
            # Defensive Programming
            if rating < 0:
                rating = 0
            elif rating > 5:
                rating = 5

            # HTML for the golden ratings stars
            if rating:
                stars_html = (('<i class="fas fa-star mr-1" '
                              'style=" color:goldenrod;"></i>') * rating)
                reviews[i]['rating'] = stars_html

            # Has the user already written a review for this poster?
            if (request.user.is_authenticated and
               request.user.id == reviews[i]['user_id'] and
               theposter_id == reviews[i]['poster_id']):
                review_index = i

    if not request.user.is_authenticated:
        # User not logged in - show NO editing options
        return (
            add_review_possible,
            update_review_possible,
            review_id,
            reviews
        )

    # Has the user already written a review for this poster?
    if review_index > -1:
        """
        Reorder the list so that the user's review APPEARS FIRST.
        Display the 'Review - Edit|Delete' option
        """
        if review_index != 0:
            review = reviews.pop(review_index)
            reviews.insert(0, review)

        # Now the review in question is at index 0
        review_id = reviews[0]['id']
        update_review_possible = True
        return (
            add_review_possible,
            update_review_possible,
            review_id,
            reviews
        )

    # Has the user purchased the poster in question?
    if (UserPurchasedPosters.objects.filter(user=request.user,
                                            poster=theposter)
                            .exists()):
        # Display the 'Review - Add' option
        add_review_possible = True

    return (
        add_review_possible,
        update_review_possible,
        review_id,
        reviews
    )


@login_required
def add_poster(request):
    """ Add a poster to the store """
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            poster = form.save()
            messages.success(request, 'Successfully added poster!')
            return redirect(reverse('poster_details', args=[poster.id]))
        else:
            messages.error(request, ('Failed to add poster. '
                                     'Please ensure the form is valid.'))
    else:
        form = PosterForm()

    template = 'posters/add_poster.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_poster(request, poster_id):
    """ Edit a poster in the store """
    poster = get_object_or_404(Poster, pk=poster_id)
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES, instance=poster)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated poster!')
            return redirect(reverse('poster_details', args=[poster.id]))
        else:
            messages.error(request, ('Failed to update poster. '
                                     'Please ensure the form is valid.'))
    else:
        form = PosterForm(instance=poster)
        messages.info(request, f'You are editing {poster.name}')

    template = 'posters/edit_poster.html'
    context = {
        'form': form,
        'poster': poster,
    }

    return render(request, template, context)


@login_required
def delete_poster(request, poster_id):
    """ Delete a poster from the store """
    poster = get_object_or_404(Poster, pk=poster_id)
    if request.method == 'POST':
        poster.delete()
        messages.success(request, 'Poster successfully deleted!')
        return redirect(reverse('posters'))

    context = {'poster': poster}
    return render(request, 'posters/delete_poster.html', context)
