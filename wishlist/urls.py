from django.urls import path
from . import views

urlpatterns = [
    path('add_to_wishlist/', views.add_to_wishlist,
         name='add_to_wishlist'),
    path('remove_from_wishlist/',
         views.remove_from_wishlist, name='remove_from_wishlist'),
    path('my_wishlist/',
         views.my_wishlist, name='my_wishlist'),
    path('remove_from_list/<int:poster_id>/',
         views.remove_from_wishlist_page, name='remove_from_wishlist_page'),
]
