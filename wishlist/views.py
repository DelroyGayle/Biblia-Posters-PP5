from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wishlist.models import Wishlist
from posters.models import Poster


@login_required
def add_to_wishlist(request):
    """ Add poster to user's wishlist """
    current_poster_path = request.session.get('current_poster_path')
    poster_id = request.session.get('poster_id')
    the_poster = get_object_or_404(Poster, pk=poster_id)
    # Create and Save to Wishlist
    wishlist = (
        Wishlist.objects.create(user=request.user, poster=the_poster)
    )
    messages.success(request, 'Poster added to wishlist!')
    return redirect(current_poster_path)


@login_required
def remove_from_wishlist(request):
    """ Remove poster from user's wishlist """
    poster_id = request.session.get('poster_id')
    (Wishlist.objects.filter(user=request.user.id,
                             poster=poster_id).delete()
     )
    messages.success(request, 'Poster removed from wishlist!')
    current_poster_path = request.session.get('current_poster_path')
    return redirect(current_poster_path)
