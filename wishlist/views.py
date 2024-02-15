from django.shortcuts import redirect, render, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wishlist.models import Wishlist
from posters.models import Poster


@login_required
def add_to_wishlist(request):
    """ Add poster to user's wishlist """
    poster_id = request.session.get('poster_id')
    the_poster = get_object_or_404(Poster, pk=poster_id)
    # Create and Save to Wishlist
    wishlist = (
        Wishlist.objects.create(user=request.user, poster=the_poster)
    )
    messages.info(request, 'Poster added to wishlist!')
    # Redisplay the Poster Details Page
    return redirect(reverse('poster_details', args=[poster_id]))


@login_required
def remove_from_wishlist(request):
    """ Remove poster from user's wishlist """
    poster_id = request.session.get('poster_id')
    (Wishlist.objects.filter(user=request.user.id,
                             poster=poster_id).delete()
     )
    messages.info(request, 'Poster removed from wishlist!')
    # Redisplay the Poster Details Page
    return redirect(reverse('poster_details', args=[poster_id]))


@login_required
def my_wishlist(request):
    """ Display the user's wishlist """

    from posters.views import reset_session_variables

    reset_session_variables(request)  # Ensure Reset!
    # Retrieve the user's wishlist
    posters = (Wishlist.objects.filter(user=request.user.id)
                               .order_by('-created_at')
               )

    context = {
        'posters': posters,
    }
    return render(request, 'wishlist/my_wishlist.html', context)


@login_required
def remove_from_wishlist_page(request, poster_id):
    """ Remove poster from user's wishlist """
    (Wishlist.objects.filter(user=request.user.id,
                             poster=poster_id).delete()
     )
    messages.info(request, 'Poster removed from wishlist!')
    # Rerender the My Wishlist Page
    return my_wishlist(request)
