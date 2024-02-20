from django.db import models
from django.db.models import CheckConstraint, Q, F


class SpecialDays(models.Model):
    """
    Model used to record the range of days
    whereby 25% Discount is offered
    """

    from django.core.validators import MaxValueValidator, MinValueValidator

    special_days_firstday = models.DateTimeField()
    special_days_lastday = models.DateTimeField()
    special_days_id = models.IntegerField(null=False,
                                          default=0,
                                          validators=[MinValueValidator(0),
                                                      MaxValueValidator(2)])

    class Meta:
        ordering = ['special_days_firstday']
        verbose_name_plural = "Special Days"

        constraints = [
            models.CheckConstraint(check=models.Q(special_days_lastday__gte=(
                F('special_days_firstday'))),
                                   name='check_date_range'),
        ]
