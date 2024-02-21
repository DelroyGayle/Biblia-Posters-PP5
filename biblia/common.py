class Common:
    """
    I use this class as the repository of global variables, settings
    and methods needed throughout this App.
    """

# Class Variables
    purchased_posters_list = None
    today_checked = None
    special_day_today = None
    special_days_queryset = None
    specials_days_name = None
    infoline = None

    def __init__(self):
        pass


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
    # TODO DG
    A context processor to check if today is a 'special day!'
    For this Project, the Special Days are defined
    as Passover, Pentecost and the Feast of Booths

    The relevants date ranges are stored in the 'SpecialDays' database
    """

    define_special_days_queryset(request)

    result = Common.special_days_queryset.first()

    print("R0", Common.today_checked, Common.special_day_today, result)

    # TEST - DISCOUNT ALWAYS ON

    Common.today_checked = True
    Common.special_day_today = True

    the_name = 'Pentecost'  # TODO DG
    the_banner = f' - {the_name} - 25% Discount Today!'
    # TODO REPEATED BELOW

    request.session['special_days_name'] =  the_name
    context = {
                'special_days_name': the_name,
                'special_days_banner': the_banner,
    }
    return context

    # TODO

    if not result:
        Common.today_checked = False
        Common.special_day_today = False
        return {}

    the_index = queryset.first().id
    print("ID", the_index)
    the_name = settings.SPECIAL_DAYS_NAMES[the_index]
    the_name = 'Feast of Booths'  # TODO DG
    the_banner = f' - {the_name} - 25% Discount Today!'

    Common.today_checked = True
    Common.special_day_today = True

    context = {
                'special_days_name': the_name,
                'special_days_banner': the_banner,
    }
    return context
