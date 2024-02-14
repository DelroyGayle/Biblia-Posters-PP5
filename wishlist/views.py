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
    messages.success(request, 'Poster added to wishlist!')
    # Show message WITHOUT displaying shopping bag contents
    request.session['show_no_bag'] = True
    return redirect(reverse('poster_details', args=[poster_id]))


@login_required
def remove_from_wishlist(request):
    """ Remove poster from user's wishlist """
    poster_id = request.session.get('poster_id')
    (Wishlist.objects.filter(user=request.user.id,
                             poster=poster_id).delete()
     )
    # Show message WITHOUT displaying shopping bag contents
    messages.success(request, 'Poster removed from wishlist!')
    request.session['show_no_bag'] = True
    return redirect(reverse('poster_details', args=[poster_id]))


@login_required
def my_wishlist(request):
    """ Display the user's wishlist """

    # Retrieve the user's wishlist
    posters = Wishlist.objects.filter(user=request.user.id).order_by('-created_at')

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
    # Show message WITHOUT displaying shopping bag contents
    # messages.success(request, 'Poster removed from wishlist!')
    #request.session['show_no_bag'] = True
    # return render(request, 'wishlist/my_wishlist.html', {})
    return my_wishlist(request)
