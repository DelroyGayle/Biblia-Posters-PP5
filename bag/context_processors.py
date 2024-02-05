from decimal import Decimal
from django.conf import settings

"""A context processor to return the contents of the shopping bag """
def bag_contents(request):

    bag_items = []
    total = 0
    poster_count = 0
   
    grand_total = total + settings.DELIVERY_COST if total>0 else total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'poster_count': poster_count,
        'grand_total': grand_total,
    }

    return context