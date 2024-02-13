from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from posters.models import Poster
from reviews.models import Review

from .forms import ReviewForm


@login_required
def add_review(request):
    """ Add a review """
    current_poster_path = request.session.get('current_poster_path')
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
            # trim the fields
            review.user_displayed_name = review.user_displayed_name.strip()
            review.title = review.title.strip()
            review.content = review.content.strip()
            # Save the new review
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(current_poster_path)
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
        'current_poster_path': current_poster_path,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review """

    the_review = get_object_or_404(Review, pk=review_id)
    current_poster_path = request.session.get('current_poster_path')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=the_review)
        if form.is_valid():
            review = form.save(commit=False)
            # trim the fields
            review.user_displayed_name = review.user_displayed_name.strip()
            review.title = review.title.strip()
            review.content = review.content.strip()
            # Update the review
            review.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(current_poster_path)
        else:
            messages.error(request, (
                'Failed to update review. '
                'Please ensure the form is valid. '
                'Rating must be a number in the range '
                '0 to 5')
            )

    else:
        form = ReviewForm(instance=the_review)
        messages.info(request, f'You are editing {the_review.title}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': the_review,
        'current_poster_path': current_poster_path,
    }

    return render(request, template, context)
