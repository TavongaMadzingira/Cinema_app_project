from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', movie_list),
    path('movies/<int:pk>/', movie_detail),
    path('trending/', trending_movies),
]