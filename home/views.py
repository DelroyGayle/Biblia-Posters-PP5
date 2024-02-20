from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    from posters.views import reset_session_variables
    
    from biblia.common import Common
    from biblia.common import checkfor_special_days


    reset_session_variables(request)  # Ensure Reset!

    # Check if today is a Special Day
    if not Common.today_checked:
        checkfor_special_days(request)

    return render(request, 'home/index.html')
