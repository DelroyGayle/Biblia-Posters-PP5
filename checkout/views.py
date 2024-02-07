from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 
                       "There's nothing in your bag at the moment")
        # redirect back to the posters page
        return redirect(reverse('posters'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OUTZrHPvBtuEw4nlFFEsWmygw30ndXtlT9zC9tOHGuJCpOVoYhBjxXq2kA2GSV9oh53JPjrTVsduoGJGEkXzgDx00edeu7wSX',
        'client_secret': 'test client secret',        
    }

    return render(request, template, context)
