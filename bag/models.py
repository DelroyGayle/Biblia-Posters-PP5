from django.db import models
from django.db.models import CheckConstraint, Q, F

# Create your models here.

class SpecialDays(models.Model):
    """ 
    Model used to record the range of days
    whereby 25% Discount is offered
    """
    special_days_firstday = models.DateField()
    special_days_lastday = models.DateField()
    special_days_id = models.IntegerField(null=False, blank=False,
                                          default=0)

    class Meta:
        ordering = ['special_days_firstday']
        verbose_name_plural = "Special Days"

        constraints = [
            models.CheckConstraint(check=models.Q(special_days_lastday__gte=F('special_days_firstday')),
                                   name = 'check_date_range'),
        ]
