from django.urls import path
from . import views

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/',
         views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/',
         views.delete_review, name='delete_review'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('edit_from_list/<int:review_id>/',
         views.edit_review_from_list, name='edit_review_from_list'),
    path('remove_review/<int:review_id>/',
         views.remove_from_reviews_page, name='remove_review'),
]
