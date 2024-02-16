from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fetch_posters, name='posters'),
    path('<int:poster_id>/', views.poster_details, name='poster_details'),
    path('add/', views.add_poster, name='add_poster'),
    path('reviews/', include('reviews.urls')),
]
