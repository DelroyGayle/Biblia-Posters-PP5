from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings

from bag.context_processors import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from posters.models import Poster

import stripe


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
            # Save the Order to the Database
            order = order_form.save()
            # Iterate through the Bag's Contents
            # Save each Order Line to the Database
            print(bag.items())
            for item_id, item_data in bag.items():
                try:
                    poster_instance = Poster.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            poster=poster_instance,
                            quantity=item_data,
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
    messages.success(request, (f'Order successfully processed! '
        f'Your order number is {order_number}. A confirmation '
        f'email will be sent to {order.email}.'))

    # delete the user shopping bag from the session
    if 'bag' in request.session:
        del request.session['bag']


    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # return the user to the successful order page
    return render(request, template, context)
