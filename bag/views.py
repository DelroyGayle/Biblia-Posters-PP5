from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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

    # Store in session variable
    request.session['bag'] = bag
    
    return redirect(currentpage_url)
