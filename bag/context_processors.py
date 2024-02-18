from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from posters.models import Poster
from bag.models import SpecialDays

"""A context processor to return the contents of the shopping bag """
def bag_contents(request):

    bag_items = []
    total = Decimal(0)
    poster_count = 0
    # Fetch the shopping bag's contents
    # Initialise to {} if empty!
    bag = request.session.get('bag', {})
    # TODO DG
    if 'special_day_today' in request.session:
        discount_factor = settings.DISCOUNT_FACTOR
    else:
        discount_factor = 1

    # tally up the total cost and poster count
    # Calculate and record the subtotal
    for item_id, quantity in bag.items():
        poster_instance = get_object_or_404(Poster, pk=item_id)
        subtotal = quantity * poster_instance.price * discount_factor
        total += subtotal
        poster_count += quantity
        # add the posters and their data to the bag items list
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'poster': poster_instance,
            'subtotal': subtotal,
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
    # TODO USE Common
    # REMOVE DF
    if 'special_day_today' in request.session:
        context |= {'discount_factor': settings.DISCOUNT_FACTOR}

    return context


"""
A context processor to check if today is a 'special day!' 
For this Project, the Special Days are defined 
as Passover, Pentecost and the Feast of Booths

The relevants date ranges are stored in the 'SpecialDays' database
"""

def checkfor_special_days(request):
    from datetime import date, timedelta

    # TODO DG
    todays_date = date.today()
    # print(todays_date, type(todays_date))
    # print(todays_date + timedelta(days=1))
    # print(todays_date + timedelta(days=-1))
    # print(todays_date + timedelta(hours=1))
    # print(todays_date + timedelta(hours=-1))
    # print(todays_date + timedelta(minutes=30))
    # print(todays_date + timedelta(minutes=-30))

    # TODO DG
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date))
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).count())
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).exists())
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).first())

    print(todays_date.strftime('%d %B %Y %I:%M'), (date(2024,2,17) + timedelta(minutes=1445)).strftime('%d %B %Y %I:%M'))
    if (SpecialDays.objects.filter(special_days_firstday__lte=todays_date + timedelta(minutes=45), 
        special_days_lastday__gte=todays_date + timedelta(minutes=45)).first()):
        print("FIRST EXISTS")
    else:
        print("NONE")

    queryset = (SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).first())

    if not queryset:
        request.session['today_checked'] = False
        request.session['special_day_today'] = False
        return {}

    the_index = queryset.special_days_id
    the_name = settings.SPECIAL_DAYS_NAMES[the_index]
    the_name = 'Feast of Booths' # TODO DG
    the_banner = f' - {the_name} - 25% Discount Today!'
    request.session['today_checked'] = True
    request.session['special_day_today'] = True

    context = {
                'special_days_name': the_name,
                'special_days_banner': the_banner,
    }
    return context

    #     'total': total,
    #     'poster_count': poster_count,
    #     'grand_total': grand_total,
    #     'delivery_cost': settings.DELIVERY_COST
    # } TODO DG

    return {} # {'todays_date': todays_date} # TODO DG