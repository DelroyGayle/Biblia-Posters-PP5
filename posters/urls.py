from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fetch_posters, name='posters'),
    path('<int:poster_id>/', views.poster_details, name='poster_details'),
    path('add_poster/', views.add_poster, name='add_poster'),
    path('edit_poster/<int:poster_id>/',
         views.edit_poster, name='edit_poster'),
    path('delete_poster/<int:poster_id>/',
        views.delete_poster, name='delete_poster'),
    path('reviews/', include('reviews.urls')),
]
