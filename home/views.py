from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    from bag.context_processors import checkfor_special_days

    from posters.views import reset_session_variables

    from biblia.common import Common

    reset_session_variables(request)  # Ensure Reset!

    # Check if today is a Special Day
    if not Common.today_checked:
        checkfor_special_days(request)

    return render(request, 'home/index.html')


def privacy(request):
    """
    A view to the Privacy page
    """
    return render(request, "home/privacy.html")
