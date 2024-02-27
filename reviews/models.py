from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from posters.models import Poster


class Review(models.Model):
    """
    This model is used for storing and maintaining
    User's Poster Reviews
    Only users who have purchased the poster in question
    can review it.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    amended_at = models.DateField(auto_now=True)
    user_displayed_name = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=80)
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5,
                                         validators=[MinValueValidator(0),
                                                     MaxValueValidator(5)])

    def __str__(self):
        return self.title
