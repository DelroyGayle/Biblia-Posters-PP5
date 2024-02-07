from django.db import models

# Create your models here.

import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django.contrib.auth.models import User
from posters.models import Poster


class Order(models.Model):
    """ Model used to record all orders """
    order_number = models.CharField(max_length=32,
                                    null=False, editable=False)
    full_name = models.CharField(max_length=50,
                                 null=False, blank=False)
    email = models.EmailField(max_length=60,
                              null=False, blank=False)
    phone_number = models.CharField(max_length=20,
                                    null=False, blank=False)
    country = models.CharField(max_length=40,
                               null=False, blank=False)
    postcode = models.CharField(max_length=20,
                                null=True, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        That is, a random string of 32 characters
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        The sum function is used to sum up all the line-item total fields
        for all line items on this order.
        The result will be in a new field called lineitem_total_sum
        TODO/PRINT  print(aggregate_sum)
        """
        aggregate_sum = self.lineitems.aggregate(Sum('lineitem_total'))
        self.order_total = aggregate_sum['lineitem_total__sum']
        self.delivery_cost = settings.DELIVERY_COST
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it has not been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ Model used to record each line of an order """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    poster = models.ForeignKey(Poster, null=False, blank=False,
                               on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.poster.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.poster.sku} on order {self.order.order_number}'


class UserPurchasedPosters(models.Model):
    """
    Model used to record 'by user' the posters that the user had purchased.
    This is used to give verified purchasers the functionality
    to add a review regarding the purchased poster.
    This is recorded in order to verify that the user has purchased a poster
    in order to allow the user to add a review about the purchased poster
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    poster = models.OneToOneField(Poster, on_delete=models.CASCADE)

    def __str__(self):
        return f'self.user.get_username() purchased SKU {self.poster.sku}'