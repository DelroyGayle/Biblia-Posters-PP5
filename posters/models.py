from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=40)
    friendly_name = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Poster(models.Model):
    """
    This model is used for storing and maintaining Posters
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 null=True, blank=True,
                                 default=5,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
