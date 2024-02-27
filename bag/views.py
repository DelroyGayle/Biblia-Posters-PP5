from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from posters.models import Poster

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    from bag.context_processors import checkfor_special_days

    from biblia.common import Common

    # Check if today is a Special Day
    if not Common.today_checked:
        _ = checkfor_special_days(request)

    theposter = get_object_or_404(Poster, pk=item_id)
    # Convert string value into an integer
    quantity = int(request.POST.get('quantity'))
    currentpage_url = request.POST.get('redirect_url')
    # Fetch the current contents of this session's shopping bag
    # Default value is {} if None
    bag = request.session.get('bag', {})

    # If the item already is in the bag update the quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, (f'Updated {theposter.name} quantity '
                                   f'to {bag[item_id]}'))
    else:
        # Add item and its quantity to the bag
        bag[item_id] = quantity
        messages.success(request, f'Added {theposter.name} to your bag')

    # Update session variable
    request.session['bag'] = bag

    return redirect(currentpage_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    RANGE_MIN = 0
    RANGE_MAX = 99

    theposter = get_object_or_404(Poster, pk=item_id)
    try:
        quantity = int(request.POST.get('quantity'))

        # Is it a legal quantity i.e. within the 1-99 range?
        if quantity > RANGE_MAX:
            messages.error(request,
                           f"Value must be less than or equal to {RANGE_MAX}")
            return redirect(reverse('view_bag'))
        elif quantity < RANGE_MIN:
            messages.error(request,
                           ("Value must be greater than or equal to "
                            f"{RANGE_MIN}"))
            return redirect(reverse('view_bag'))
    except ValueError:
        # Erroneous Input
        messages.error(request,
                       "Please enter a number")
        return redirect(reverse('view_bag'))

    # Fetch the current contents of this session's shopping bag
    # Default value is {} if None
    bag = request.session.get('bag', {})
    # Update new quantity
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, (f'Updated {theposter.name} quantity '
                                   f'to {bag[item_id]}'))

    else:
        # Zero entered therefore remove the item entirely
        bag.pop(item_id)
        messages.success(request, (f'Removed {theposter.name} quantity '
                                   'from your bag'))

    # Update session variable
    request.session['bag'] = bag
    # Reload page with the Shopping Bag contents
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    Because this view will be posted to a JavaScript function,
    an actual HTTP response is returned instead.
    200 for Success
    500 if an error occurs
    """

    try:
        theposter = get_object_or_404(Poster, pk=item_id)
        # Fetch the current contents of this session's shopping bag
        # Default value is {} if None
        bag = request.session.get('bag', {})
        # remove the item entirely
        bag.pop(item_id)
        messages.success(request, (f'Removed {theposter.name} quantity '
                                   'from your bag'))
        # Update session variable
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        # An error has occurred, therefore display a custom 500 page TODO
        return HttpResponse(status=500)
