from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from posters.models import Poster


class Wishlist(models.Model):
    """
    This model is used for storing and maintaining
    posters on a user's wishlist
    Only registered users can use wishlist functionality
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        username = self.user.get_username()
        theposter = get_object_or_404(Poster, pk=self.poster_id)
        return (f'{username} listed '
                f'POSTER ID: {theposter.id} '
                f'Name: {theposter.name}')
