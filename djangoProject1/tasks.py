from celery import shared_task
from models import Movie

@shared_task
def update_movie_ranking():
    movies = Movie.objects.filter(status='upcoming')
    for movie in movies:
        movie.ranking += 10
        movie.save()
