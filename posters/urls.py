from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posters, name='posters'),
    path('<poster_id>', views.poster_details, name='poster_details'),
]