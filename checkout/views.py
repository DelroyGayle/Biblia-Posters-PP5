from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from bag.context_processors import bag_contents
from .forms import OrderForm

import stripe


def checkout(request):
    stripePublicKey = settings.STRIPE_PUBLIC_KEY
    stripeSecretKey = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                       "There's nothing in your bag at the moment")
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
            "Did you forget to set it in your environment?"))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripePublicKey,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
