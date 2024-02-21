from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from posters.models import Poster


def bag_contents(request):
    """A context processor to return the contents of the shopping bag """

    from biblia.common import Common

    if Common.special_day_today:
        # Apply discount if it is a 'Special Day' Today
        discount_factor = settings.DISCOUNT_FACTOR
    else:
        # Otherwise no discount
        discount_factor = 1

    bag_items = []
    total = Decimal(0)
    poster_count = 0
    # Fetch the shopping bag's contents
    # Initialise to {} if empty!
    bag = request.session.get('bag', {})

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


def define_special_days_queryset(request):
    """
    This Queryset is used to determine whether
    Today's Date is a Special Day

    The Query checks whether Today's Date is between the range of
    'special_days_firstday' and 'special_days_lastday'
    However, a tolerance of 30 minutes is given for both of these
    time values to cater for the user either
    1) coming to the website minutes before midnight
    just prior to when the Specials Days Range starts
    2) or coming to the website minutes before midnight
    just prior to when the Specials Days Range ends
    """

    from django.db.models import Q
    from django.db.models import F, DateTimeField, ExpressionWrapper
    from django.utils import timezone

    from bag.models import SpecialDays

    from datetime import timedelta

    from biblia.common import Common

    if Common.special_days_queryset is not None:
        # Queryset has already been set up
        return

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
    Common.special_days_queryset = queryset


def checkfor_special_days(request):
    """
    A context processor to check if today is a 'special day!'
    For this Project, the Special Days are defined
    as Passover, Pentecost and the Feast of Booths

    The relevants date ranges are stored in the 'SpecialDays' database
    """

    from biblia.common import Common

    define_special_days_queryset(request)

    result = Common.special_days_queryset.first()

    # TODO
    # the_index = queryset.first().id
    the_index = 0

    # TEST - DISCOUNT ALWAYS ON TODO DG

    Common.today_checked = True
    Common.special_day_today = True

    the_name = 'Passover'  # TODO DG
    the_banner = f' - {the_name} - 25% Discount Today!'
    request.session['special_days_name'] = the_name
    context = {
                'special_days_name': the_name,
                'special_days_banner': the_banner,
    }
    return context

    # TODO DG

    if not result:
        Common.today_checked = False
        Common.special_day_today = False
        request.session.pop('special_days_namers', None)
        return {}

    Common.today_checked = True
    Common.special_day_today = True

    the_index = queryset.first().id
    print("ID", the_index)  # TODO DEFENSIVE
    the_name = settings.SPECIAL_DAYS_NAMES[the_index]
    the_banner = f' - {the_name} - 25% Discount Today!'
    request.session['special_days_name'] = the_name
    context = {
                'special_days_name': the_name,
                'special_days_banner': the_banner,
    }
    return context
