from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from bag.context_processors import bag_contents

from .forms import OrderForm
from .models import Order, OrderLineItem
from posters.models import Poster
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from checkout.models import UserPurchasedPosters

from biblia.common import Common

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                       'processed right now. Please try again later.'))
        return HttpResponse(content=e, status=400)


def handle_POST_method(request):
    """ Regarding Checkout, a POST Method has been requested """

    bag = request.session.get('bag', {})
    if Common.special_day_today:
        # Apply discount if it is a 'Special Day' Today
        discount_factor = settings.DISCOUNT_FACTOR
    else:
        # Otherwise no discount
        discount_factor = 1

    form_data = {
        'full_name': request.POST['full_name'],
        'email': request.POST['email'],
        'phone_number': request.POST['phone_number'],
        'country': request.POST['country'],
        'postcode': request.POST['postcode'],
        'city': request.POST['city'],
        'street_address1': request.POST['street_address1'],
        'street_address2': request.POST['street_address2'],
        'county': request.POST['county'],
    }
    order_form = OrderForm(form_data)
    if order_form.is_valid():
        # Valid Order - Add Unique Stripe PID before saving
        order = order_form.save(commit=False)
        pid = request.POST.get('client_secret').split('_secret')[0]
        order.stripe_pid = pid
        order.original_bag = json.dumps(bag)
        if Common.special_day_today:
            order.special_days_discount_name = (
                   request.session['special_days_name'])
        # Save the Order to the Database
        order.save()

        # Iterate through the Bag's Contents
        # Save each Order Line to the Database
        # Keep a list of each poster purchased
        posters_list = []
        for item_id, item_quantity in bag.items():
            try:
                poster_instance = Poster.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                        order=order,
                        poster=poster_instance,
                        quantity=item_quantity,
                    )
                order_line_item.save(discount_factor=discount_factor)
                # Record the purchased poster
                posters_list.append(poster_instance)

            except Poster.DoesNotExist:

                messages.error(request, (
                    "One of the posters in your bag was not "
                    "found in our database. "
                    f"POSTER ID Number {id}"
                    "Please call us for assistance!")
                )
                # Invalid/Missing Poster therefore delete the Order
                order.delete()
                return redirect(reverse('view_bag'))

        """
        Check whether or not the user wants to save their
        profile information to the session
        """
        request.session['save_info'] = ('save-info'
                                        in request.POST)

        """
        Save the list of all purchased posters
        for Reviews purposes
        """
        if request.user.is_authenticated:
            # Indicate that Purchased Posters have been found
            Common.purchased_posters_list = posters_list
            request.session['purchased_posters'] = True
        else:
            # Just in case these have exists or have values
            Common.purchased_posters_list = None
            request.session.pop('purchased_posters', None)

        # Success Page
        return redirect(reverse('checkout_success',
                                args=[order.order_number]))
    else:

        # Invalid Form
        messages.error(request, ("There was an error with your form. ",
                                 "Please double check your information."))

    return None


def handle_GET_method(request, stripeSecretKey):
    """ Regarding Checkout, a GET Method has been requested """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                       "There is nothing in your bag at the moment")
        # redirect back to the posters page
        newpage = redirect(reverse('posters'))
        return (newpage,)  # Tuple of ONE item

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripeSecretKey
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Attempt to prefill the form with any info
    # the user maintains in their profile
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)

            # Populate the Full Name from the User model
            # if the Profile Full Name is null
            the_fullname = profile.user.get_full_name()
            if not the_fullname:
                the_fullname = request.user.get_username()

            # Populate the Email Address from the User model
            # if the Profile Email Address is null
            the_email = profile.user.email
            if not the_email:
                the_email = request.user.email

            order_form = OrderForm(initial={
                'full_name': the_fullname,
                'email': the_email,
                'phone_number': profile.default_phone_number,
                'country': (profile.default_country
                            or settings.UK_ISO_3166_VALUE),
                'postcode': profile.default_postcode,
                'city': profile.default_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })

        except UserProfile.DoesNotExist:
            order_form = OrderForm()

    else:
        order_form = OrderForm()

    return (None, order_form, intent)


def checkout(request):
    """
    Secure Checkout has been selected
    This Method communicates with Stripe
    in order to perform a secure purchase of the order
    """
    stripePublicKey = settings.STRIPE_PUBLIC_KEY
    stripeSecretKey = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # POST Method requested
        newpage = handle_POST_method(request)
        if newpage:
            # New Page returned therefore this will be
            # the new page that the user will view
            return newpage

    else:
        # GET Method requested
        result = handle_GET_method(request, stripeSecretKey)
        newpage, *two_parameters = result  # Unpack First Item Only
        if newpage:
            # New Page returned therefore this will be
            # the new page that the user will view
            return newpage

        (order_form, intent) = two_parameters

    if not stripePublicKey:
        messages.warning(request, ("Stripe public key is missing. "
                                   "Did you forget to set it in "
                                   "your environment?"))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripePublicKey,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def record_each_poster(request):
    """
    Store a record of every poster purchased
    by each registered user - for Reviews purposes
    """

    for eachposter in Common.purchased_posters_list:
        obj, created = UserPurchasedPosters.objects.get_or_create(
                user=request.user,
                poster=eachposter)


def reset_special_days_variables():
    """
    After each successful order reset these fields
    So that a new check is made of
    whether the day of a new order is a special day
    """

    Common.today_checked = None
    Common.special_day_today = None
    Common.special_days_queryset = None


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    # At this point the order was successful
    # Therefore if the user is logged in
    # Attach the user's profile to the order at this point
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
        # Record the user with each poster purchased
        purchased_posters = request.session.get('purchased_posters')
        if purchased_posters:
            record_each_poster(request)
            # Reset
            request.session.pop('purchased_posters', None)
            Common.purchased_posters_list = None

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Reset the fields that handle Special Days
    reset_special_days_variables()

    # If today's date is a Special Day,
    # Add an infoline explaining the 25% discount

    if order.special_days_discount_name != '':
        infoline = (f'{order.special_days_discount_name}'
                    ' 25% Discount has been applied to the order')
    else:
        infoline = ''

    messages.success(request, ('Order successfully processed! '
                               f'Your order number is {order_number}. '
                               'A confirmation email will be sent to '
                               f'{order.email}.'))

    # delete the user shopping bag from the session
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    # 'infoline' informing the user about the 25% Discount
    context = {
        'order': order,
        'infoline': infoline
    }

    # return the user to the successful order page
    return render(request, template, context)
