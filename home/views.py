from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    from posters.views import reset_session_variables

    reset_session_variables(request)  # Ensure Reset!

    return render(request, 'home/index.html')
