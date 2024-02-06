from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    # Convert string value into an integer
    quantity = int(request.POST.get('quantity'))
    currentpage_url = request.POST.get('redirect_url')
    # Fetch the current contents of this session's shopping bag
    # Default value is {} if None
    bag = request.session.get('bag', {})

    # If the item already is in the bag update the quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        # Add item and its quantity to the bag
        bag[item_id] = quantity

    # Update session variable
    request.session['bag'] = bag

    return redirect(currentpage_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    # Fetch the current contents of this session's shopping bag
    # Default value is {} if None
    bag = request.session.get('bag', {})
    # Update new quantity
    if quantity > 0:
        bag[item_id] = quantity
    else:
        # Zero entered therefore remove the item entirely
        bag.pop(item_id)

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
        # Fetch the current contents of this session's shopping bag
        # Default value is {} if None
        bag = request.session.get('bag', {})
        # remove the item entirely
        bag.pop(item_id)
        # Update session variable
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        # An error has occurred - direct to a custom 500 page
        return HttpResponse(status=500)
