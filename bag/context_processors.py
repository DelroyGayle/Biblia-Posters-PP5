from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from posters.models import Poster

"""A context processor to return the contents of the shopping bag """


def bag_contents(request):
    from biblia.common import Common

    bag_items = []
    total = Decimal(0)
    poster_count = 0
    # Fetch the shopping bag's contents
    # Initialise to {} if empty!
    bag = request.session.get('bag', {})
    # TODO DG
    # if 'special_day_today' in request.session:
    #     discount_factor = settings.DISCOUNT_FACTOR
    # else:
    #     discount_factor = 1
    
    if Common.special_day_today:
        # Apply discount if it is a 'Special Day' Today
        discount_factor = settings.DISCOUNT_FACTOR
    else:
        # Otherwise no discount
        discount_factor = 1
    print('DFS', discount_factor, Common.special_day_today)

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
        'delivery_cost': settings.DELIVERY_COST,
        'discount_factor': discount_factor,
    }

    return context


"""
A context processor to check if today is a 'special day!'
For this Project, the Special Days are defined
as Passover, Pentecost and the Feast of Booths

The relevants date ranges are stored in the 'SpecialDays' database
"""


def checkfor_special_days(request):
    from django.utils import timezone
    from django.db.models import Q

    from bag.models import SpecialDays
    from django.db.models import F, DateTimeField, ExpressionWrapper
    from datetime import timedelta

    from biblia.common import Common

    todays_date = timezone.now()

    when_ranges_equal = Q(special_days_firstday=F('special_days_lastday'))
    range_start_lessthan_todays_date = Q(earlier_by_30mins__lte=todays_date)
    range_end_greaterthan_todays_date = Q(later_by_1day30mins__gte=todays_date)

    queryset = (SpecialDays.objects.annotate(
                 earlier_by_30mins=(
                     ExpressionWrapper(
                         F("special_days_firstday") - timedelta(seconds=1800),
                         output_field=DateTimeField())),
                 later_by_1day30mins=(
                     ExpressionWrapper(F("special_days_lastday") +
                                       timedelta(hours=24,
                                       seconds=1800),
                                       output_field=DateTimeField())))
                .filter(range_start_lessthan_todays_date
                        & range_end_greaterthan_todays_date)
                )

    result = queryset.first()

    print("R0", Common.today_checked, Common.special_day_today, result)

    # TEST - DISCOUNT ALWAYS ON

    Common.today_checked = True
    Common.special_day_today = True

    the_name = 'Feast of Booths'  # TODO DG
    the_banner = f' - {the_name} - 25% Discount Today!'


    context = {
                'special_days_name': the_name,
                'special_days_banner': the_banner,
    }
    return context

    if not result:
        # request.session['today_checked'] = False  # TODO DG
        # request.session['special_day_today'] = False
        Common.today_checked = False
        Common.special_day_today = False
        return {}

    the_index = queryset.first().id
    print("ID", the_index)
    the_name = settings.SPECIAL_DAYS_NAMES[the_index]
    the_name = 'Feast of Booths'  # TODO DG
    the_banner = f' - {the_name} - 25% Discount Today!'
    # request.session['today_checked'] = True
    # request.session['special_day_today'] = True
    Common.today_checked = True
    special_day_today = True

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

    return {}  # {'todays_date': todays_date} # TODO DG
