from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from posters.models import Poster


"""A context processor to return the contents of the shopping bag """
def bag_contents(request):

    bag_items = []
    total = Decimal(0)
    poster_count = 0
    # Fetch the shopping bag's contents
    # Initialise to {} if empty!
    bag = request.session.get('bag', {})

    # tally up the total cost and poster count
    for item_id, quantity in bag.items():
        poster_instance = get_object_or_404(Poster, pk=item_id)
        total += quantity * poster_instance.price
        poster_count += quantity
        # add the posters and their data to the bag items list
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'poster': poster_instance,
        })

    grand_total = total + (settings.DELIVERY_COST 
                                if total > 0 else 0)
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'poster_count': poster_count,
        'grand_total': grand_total,
        'delivery_cost': settings.DELIVERY_COST
    }

    return context