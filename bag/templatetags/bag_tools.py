from django import template

register = template.Library()


# @register.filter(name='calc_subtotal')
# def calc_subtotal(price, quantity):
#     return price * quantity


@register.simple_tag
def calc_subtotal_3args(price, quantity, discount):
    result = price * quantity * discount
    return f'{result:.2f}'
# TODO DG
