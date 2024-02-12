from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fetch_posters, name='posters'),
    path('<poster_id>', views.poster_details, name='poster_details'),
    path('reviews/', include('reviews.urls')),
]