from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from bag.context_processors import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from posters.models import Poster

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


def checkout(request):
    stripePublicKey = settings.STRIPE_PUBLIC_KEY
    stripeSecretKey = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # POST Method requested
        bag = request.session.get('bag', {})

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
            # Save the Order to the Database
            order.save()

            # Iterate through the Bag's Contents
            # Save each Order Line to the Database
            for item_id, item_quantity in bag.items():
                try:
                    poster_instance = Poster.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            poster=poster_instance,
                            quantity=item_quantity,
                        )
                    order_line_item.save()

                except Poster.DoesNotExist:

                    messages.error(request, (
                        "One of the posters in your bag was not "
                        "found in our database. "
                        f"ID Number {id}"
                        "Please call us for assistance!")
                    )
                    # Invalid/Missing Poster therefore delete the Order
                    order.delete()
                    # return the user to the shopping bag page
                    return redirect(reverse('view_bag'))

            """
            Check whether or not the user wants to save their
            profile information to the session
            """
            request.session['save_info'] = ('save-info'
                                            in request.POST)
            # Success Page
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))

        else:

            # Invalid Form
            messages.error(request, ("There was an error with your form. ",
                           "Please double check your information."))
    else:
        # GET Method requested
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request,
                           "There is nothing in your bag at the moment")
            # redirect back to the posters page
            return redirect(reverse('posters'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripeSecretKey
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, ('Order successfully processed! '
                               f'Your order number is {order_number}. '
                               'A confirmation email will be sent to '
                               f'{order.email}.'))

    # delete the user shopping bag from the session
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # return the user to the successful order page
    return render(request, template, context)
