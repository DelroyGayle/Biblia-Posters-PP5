from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from posters.models import Poster
from bag.models import SpecialDays
from django.db.models import F, DateTimeField, ExpressionWrapper, DurationField
import datetime
from datetime import date
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

 # TODO
import datetime
from django.db.models.functions import Trunc
# TODO DG
from django.db.models.functions import (
       ExtractDay,
       ExtractMonth,
       ExtractQuarter,
       ExtractWeek,
       ExtractIsoWeekDay,
       ExtractWeekDay,
       ExtractIsoYear,
       ExtractYear,
   )

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
    # REMOVE DG
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
    import datetime

    # TODO DG
    todays_date = datetime.date.today()
    print("TODAYS", todays_date)
    # print(todays_date, type(todays_date))
    # print(todays_date + timedelta(days=1))
    # print(todays_date + timedelta(days=-1))
    # print(todays_date + timedelta(hours=1))
    # print(todays_date + timedelta(hours=-1))
    # print(todays_date + timedelta(minutes=30))
    # print(todays_date + timedelta(minutes=-30))

    todays_date2 = datetime.datetime.today()
    print(todays_date2.strftime('%Y-%m-%d'))
    print(todays_date2.strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

    todays_date = timezone.now()
    print(todays_date, 200)

    # TODO DG
    print(100)
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date))
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).count())
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).exists())
    print(SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).first())
    # print(101)
    # print(SpecialDays.objects.annotate(lastday_name=F('special_days_lastday'),
    # duration=F('special_days_lastday') - F('special_days_firstday'),
    # thelast = (F('special_days_lastday') + datetime.timedelta(hours=23, minutes=59, seconds=59)),
    #             output_field=DateTimeField())
    # .filter(special_days_firstday__lte=todays_date, 
    #                     special_days_lastday__gte=todays_date).all().values())    

    print(102)                    
    # todays_date = date.today()
    # print(datetime.combine(todays_date, timedelta(minutes=45)))

    # print(SpecialDays.objects.annotate(lastday_name=datetime.combine(F('special_days_lastday'), datetime.min.time()))
    # .filter(special_days_firstday__lte=todays_date, 
    #                      special_days_lastday__gte=todays_date).all().values()) 

    # x = datetime.now()
    # print(x)                        

    # print(103, (date(2024, 2, 18) + timedelta(1)).strftime('%d %B %Y %I:%M%p'))
    # print(104, (date(2024, 2, 18) + timedelta(hours=1)).strftime('%d %B %Y %I:%M%p'))
    # print(105, (date(2024, 2, 18) + timedelta(1)).strftime('%d %B %Y %I:%M%p'))
    # print(106, (date(2024, 2, 18) + timedelta(hours=1)).strftime('%d %B %Y %I:%M%p'))
    print(104)
    print(SpecialDays.objects.annotate(
          year=ExtractYear("special_days_lastday"),
          month=ExtractMonth("special_days_lastday"),
          day=ExtractDay("special_days_lastday"),
          duration=F('special_days_lastday') - timezone.now(),
          date1=ExpressionWrapper(F("special_days_firstday") - timedelta(seconds=1800), 
                            output_field=DateTimeField()),
          date2=ExpressionWrapper(F("special_days_lastday") + timedelta(seconds=1800), 
                            output_field=DateTimeField()),
          date3=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=23, seconds=59*60), 
                            output_field=DateTimeField()),
          date4=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=23, seconds=59*60) + timedelta(seconds=1800), 
                            output_field=DateTimeField())).values())
    # print(SpecialDays.objects.annotate(
    #       year=ExtractYear("special_days_lastday"),
    #       month=ExtractMonth("special_days_lastday"),
    #       day=ExtractDay("special_days_lastday"),
    #       duration=F('special_days_lastday') - F('special_days_firstday')
    #   ).query)
    # print(todays_date.strftime('%d %B %Y %I:%M'), (date(2024,2,17) + timedelta(minutes=14)).strftime('%d %B %Y %I:%M'))

    print(SpecialDays.objects.annotate(
          year=ExtractYear("special_days_lastday"),
          month=ExtractMonth("special_days_lastday"),
          day=ExtractDay("special_days_lastday"),
          duration=F('special_days_lastday') - timezone.now(),
          date1=ExpressionWrapper(F("special_days_firstday") - timedelta(seconds=1800), 
                            output_field=DateTimeField()),
          date2=ExpressionWrapper(F("special_days_lastday") + timedelta(seconds=1800), 
                            output_field=DateTimeField()),
          date3=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=23, seconds=59*60), 
                            output_field=DateTimeField()),
          date4=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=23, seconds=59*60) + timedelta(seconds=1800), 
                            output_field=DateTimeField())).query)

    print((SpecialDays.objects.annotate(
          date1=ExpressionWrapper(F("special_days_firstday") - timedelta(seconds=1800), 
                            output_field=DateTimeField()),
          date4=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=23, seconds=59*60) + timedelta(seconds=1800), 
                            output_field=DateTimeField()))
            .filter(date1__lte=todays_date, date4__gte=todays_date).query))                            
    print(105)

    if (SpecialDays.objects.annotate(
        #   year=ExtractYear("special_days_lastday"),
        #   month=ExtractMonth("special_days_lastday"),
        #   day=ExtractDay("special_days_lastday"),
        #   duration=F('special_days_lastday') - timezone.now(),
          date1=ExpressionWrapper(F("special_days_firstday") - timedelta(seconds=1800), 
                            output_field=DateTimeField()),
          date4=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=23, seconds=59*60) + timedelta(seconds=1800), 
                            output_field=DateTimeField()))
            .filter(date1__lte=todays_date, date4__gte=todays_date).first()):
        print("FIRST EXISTS")
    else:
        print("NONE")


    if (SpecialDays.objects.filter(special_days_firstday__lte=todays_date + timedelta(minutes=45), 
        special_days_lastday__gte=todays_date + timedelta(minutes=45)).first()):
        print("FIRST EXISTS")
    else:
        print("NONE")

    queryset = (SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
                        special_days_lastday__gte=todays_date).first())

    #is_equal = Q(special_days_firstday == special_days_lastday)
    #is_not_equal = Q(special_days_firstday != special_days_lastday)
  
    when_ranges_equal = Q(special_days_firstday=F('special_days_lastday'))
    range_start_lessthan_todays_date = Q(special_days_firstday__lte=todays_date)
    range_end_greaterthan_todays_date = Q(range_end_when_equal__gte=todays_date)

    queryset = SpecialDays.objects.annotate(
                 range_start_when_equal=ExpressionWrapper(F("special_days_firstday") - timedelta(seconds=1800), 
                                       output_field=DateTimeField()),
                 range_end_when_equal=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=24), 
                                output_field=DateTimeField()),
                 range_end_when_not_equal=ExpressionWrapper(F("special_days_lastday") + timedelta(hours=24, seconds=1800),
                            output_field=DateTimeField())).filter(when_ranges_equal &
                            Q(special_days_firstday__lte=todays_date) & range_end_greaterthan_todays_date)
                            # .filter(range_start_when_equal__lte=todays_date)

##### AGAIN

  
    when_ranges_equal = Q(special_days_firstday=F('special_days_lastday'))
    range_start_lessthan_todays_date = Q(earlier_by_30mins__lte=todays_date)
    range_end_greaterthan_todays_date = Q(later_by_1day30mins__gte=todays_date)

    queryset = SpecialDays.objects.annotate(
                 earlier_by_30mins =ExpressionWrapper(F("special_days_firstday") - timedelta(seconds=1800), 
                                       output_field=DateTimeField()),
                 later_by_1day30mins = ExpressionWrapper(F("special_days_lastday") + timedelta(hours=24, seconds=1800),
                                        output_field=DateTimeField())).filter(
                                            range_start_lessthan_todays_date & range_end_greaterthan_todays_date)
                            # .filter(range_start_when_equal__lte=todays_date)


    print(200)
    print(queryset.query)
    print(queryset.values())
#                             .first()

  
    # queryset = (SpecialDays.objects.filter(special_days_firstday__lte=todays_date, 
    #                     special_days_lastday__gte=todays_date).first())


    if not queryset:
        request.session['today_checked'] = False
        request.session['special_day_today'] = False
        return {}

    the_index = queryset.first().id
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