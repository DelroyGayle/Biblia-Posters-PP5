from django.shortcuts import render
from .forms import ReviewForm

def add_review(request):
    """ Add a review """
    form = ReviewForm(
        initial={'user_displayed_name': request.user.get_username()}
    )
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
