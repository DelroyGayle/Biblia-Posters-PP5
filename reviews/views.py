from django.shortcuts import render
from .forms import ReviewForm

def add_review(request):
    """ Add a review """
    # TODO
    poster_id = request.session.get('poster_id')
    current_poster_path = request.session.get('current_poster_path')
    # _ = get_object_or_404(Poster, pk=poster_id)
    form = ReviewForm(
        initial={'user_displayed_name': request.user.get_username()}
    )
    template = 'reviews/add_review.html'
    print("HELLO",current_poster_path )
    context = {
        'form': form,
        'poster_id': poster_id,
        'current_poster_path': current_poster_path
    }

    return render(request, template, context)
