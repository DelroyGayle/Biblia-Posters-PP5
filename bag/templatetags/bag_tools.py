from django import template

register = template.Library()


@register.simple_tag
def calc_subtotal_3args(price, quantity, discount):
    result = price * quantity * discount
    return f'{result:.2f}'
