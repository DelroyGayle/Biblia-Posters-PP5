from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from posters.models import Poster
from reviews.models import Review

from .forms import ReviewForm


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
def remove_from_wishlist_page(request, poster_id):
    """ Remove poster from user's wishlist """
    # (Wishlist.objects.filter(user=request.user.id,
    #                          poster=poster_id).delete()
    #  )
    messages.info(request, 'Poster removed from wishlist!')
    # Rerender the My Wishlist Page
    return my_wishlist(request)


@login_required
def add_review(request):
    """ Add a review """
    current_redirect_path = request.session.get('current_redirect_path')
    poster_id = request.session.get('poster_id')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # Update mandatory fields
            the_username = request.user.get_username()
            review.user = get_object_or_404(User, username=the_username)
            the_poster = get_object_or_404(Poster, pk=poster_id)
            review.poster = the_poster.id
            # Trim the fields
            review.user_displayed_name = review.user_displayed_name.strip()
            review.title = review.title.strip()
            review.content = review.content.strip()
            # Save the new review
            review.save()
            messages.info(request, 'Successfully added review!')
            # Have you been directed here from the My Reviews page?
            if not request.session.get('backto_myreviews', None):
                # No! Then Redisplay the Poster Details Page
                return redirect(reverse('poster_details', args=[poster_id]))
            else:
                # Yes! Redirect to the My Reviews page
                return redirect(reverse('my_reviews'))

        else:

            messages.error(request, (
                'Failed to add review. '
                'Please ensure the form is valid. '
                'Rating must be a number in the range '
                '0 to 5')
            )

    else:

        form = ReviewForm(
            initial={'user_displayed_name': request.user.get_username()}
        )

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'current_redirect_path': current_redirect_path,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review """

    the_review = get_object_or_404(Review, pk=review_id)
    current_redirect_path = request.session.get('current_redirect_path')
    poster_id = request.session.get('poster_id')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=the_review)
        if form.is_valid():
            # Valid Update
            review = form.save(commit=False)
            # trim the fields
            review.user_displayed_name = review.user_displayed_name.strip()
            review.title = review.title.strip()
            review.content = review.content.strip()
            # Update the review
            review.save()
            messages.info(request, 'Successfully updated review!')
            # Was the source of the Edit Command from the My Reviews page?
            if not request.session.get('backto_myreviews', None):
                # No! Then Redisplay the Poster Details Page
                return redirect(reverse('poster_details', args=[poster_id]))
            else:
                # Yes! Redirect to the My Reviews page
                return redirect(reverse('my_reviews'))

        else:

            # Invalid Form

            messages.error(request, (
                'Failed to update review. '
                'Please ensure the form is valid. '
                'Rating must be a number in the range '
                '0 to 5')
            )

    else:

        form = ReviewForm(instance=the_review)
        # Convert the review title into title-case
        messages.info(request, f'You are editing {the_review.title.title()}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': the_review,
        'current_redirect_path': current_redirect_path,
    }

    return render(request, template, context)


"""
With regards to Editing Reviews being selected from two sources
I tried 'DRY'
However, it was becoming too convoluted
Therefore, I chose to reproduce very similar code
when Editing is requested from the 'My Reviews' page
"""
@login_required
def edit_review_from_list(request, review_id):
    """ Edit a review from the My Reviews page """

    the_review = get_object_or_404(Review, pk=review_id)

    form = ReviewForm(instance=the_review)
    # Convert the review title into title-case
    messages.info(request, f'You are editing {the_review.title.title()}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': the_review,
        'current_redirect_path': request.path,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    the_review = get_object_or_404(Review, pk=review_id)
    current_redirect_path = request.session.get('current_redirect_path')
    poster_id = request.session.get('poster_id')

    if request.method == 'POST':
        the_review.delete()
        messages.info(request, 'Review successfully deleted!')
        # Redisplay the Poster Details Page
        return redirect(reverse('poster_details', args=[poster_id]))

    template = 'reviews/delete_review.html'
    context = {
        'review': the_review,
        'current_redirect_path': current_redirect_path,
    }
    return render(request, template, context)


@login_required
def remove_from_reviews_page(request, review_id):
    """ Delete a review from the My Reviews page """
    the_review = get_object_or_404(Review, pk=review_id)
    current_redirect_path = request.session.get('current_redirect_path')

    if request.method == 'POST':
        the_review.delete()
        messages.info(request, 'Review successfully deleted!')
        # Redisplay the My Reviews Page
        return redirect(reverse('my_reviews'))

    template = 'reviews/delete_review.html'
    context = {
        'review': the_review,
        'back_to_myreviews': True,
    }
    return render(request, template, context)


def annotate_review(review):
    """
    Add some new fields to the user's reviews list
    before displaying the list on the 'My Reviews' page
    """
    the_poster = get_object_or_404(Poster, pk=review['poster'])
    return review | {'poster_id': review['poster'],
                     'poster_name': the_poster.name,
                     'image': the_poster.image,
                     'image_url': the_poster.image.url}


@login_required
def display_myreviews(request):
    """ Display the user's My Reviews Page """
    username = request.user.get_username()
    reviews = (Review.objects.filter(user=username)
                               .order_by('-amended_at')
               )

    # Reconfigure the list
    if reviews:
        reviews = [annotate_review(review) for review in reviews.values()]  # TODO

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/my_reviews.html', context)


@login_required
def my_reviews(request):
    """ Display the user's reviews """
    from posters.views import reset_session_variables

    reset_session_variables(request)  # Ensure Reset!
    if request.method == 'GET':
        # Display the user's My Reviews Page
        return display_myreviews(request)

    """
    POST Method: In this context, the 'Edit Review' button 
    has been selected. Therefore, call the above
    Edit Review method, however, need to redirect the view
    back to the 'My Reviews' page
    Use request.session['backto_myreviews'] to indicate this
    """
    request.session['backto_myreviews'] = True
    review_id = request.POST['review_id']
    return edit_review_from_list(request, review_id)
