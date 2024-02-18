from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    from posters.views import reset_session_variables
    from bag.context_processors import checkfor_special_days

    reset_session_variables(request)  # Ensure Reset!
    if 'today_checked' not in request.session:
        _ = checkfor_special_days(request)


    print('td', 'today_checked' in request.session) # TODG DG USE COMMON
    return render(request, 'home/index.html')
