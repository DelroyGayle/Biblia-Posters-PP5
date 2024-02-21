from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from posters.views import reset_session_variables


@login_required
def profile(request):
    """ Display the user's profile. """

    reset_session_variables(request)  # Ensure Reset!
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated profile!')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    # Show orders with the recent at the top
    orders = profile.orders.order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # If today's date is a Special Day,
    # Add an infoline explaining the 25% discount

    if order.special_days_discount_name != '':
        infoline = (f'{order.special_days_discount_name}'
                    ' 25% Discount has been applied to the order')
    else:
        infoline = ''

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    # 'infoline' informing the user about the 25% Discount
    context = {
        'order': order,
        'from_profile': True,
        'infoline': infoline
    }

    return render(request, template, context)
