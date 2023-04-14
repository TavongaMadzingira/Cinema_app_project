from ninja import Router, Schema
from ninja.responses import JsonResponse
from models import Movie


class MovieSchema(Schema):
    name: str
    protagonists: str
    poster: str
    start_date: str
    status: str
    ranking: int


router = Router()


@router.post('/movies/')
def add_movie(request, movie: MovieSchema):
    new_movie = Movie(**movie.dict())
    new_movie.save()
    return JsonResponse({'message': 'Movie added successfully'})


@router.get('/movies/trending/')
def get_trending_movies(request):
    movies = Movie.objects.filter(status='running').order_by('-ranking')
    movie_data = []
    for movie in movies:
        movie_dict = {
            'name': movie.name,
            'protagonists': movie.protagonists,
            'poster': str(movie.poster),
            'start_date': movie.start_date,
            'status': movie.status,
            'ranking': movie.ranking,
        }
        movie_data.append(movie_dict)
    return JsonResponse(movie_data)
