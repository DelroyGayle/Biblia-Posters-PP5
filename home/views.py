from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    from posters.views import reset_session_variables
    from bag.context_processors import checkfor_special_days
    from biblia.common import Common    

    reset_session_variables(request)  # Ensure Reset!
    # TESTING RESET TD - TODO DG
    #request.session.pop('today_checked', None)
    #request.session.pop('special_day_today', None)
    print("RESET")

    # if 'today_checked' not in request.session:
    #     _ = checkfor_special_days(request)


    if not Common.today_checked:
        _ = checkfor_special_days(request)

    print('td', 'today_checked' in request.session) # TODG DG USE COMMON
    print('td2', Common.today_checked) # TODG DG USE COMMON

    return render(request, 'home/index.html')
