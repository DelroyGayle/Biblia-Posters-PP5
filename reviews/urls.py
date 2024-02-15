from django.urls import path
from . import views

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    # path('remove_review/<int:poster_id>/',
    #      views.remove_from_reviews_page, name='remove_from_reviews_page'),
]