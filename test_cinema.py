import pytest
from datetime import datetime, timedelta
from bson import ObjectId
from django.test import Client
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from requests import post


@pytest.fixture(scope='module')
def db():
    client = MongoClient()
    yield client.cinema
    client.drop_database('cinema')


@pytest.fixture(scope='module')
def api_client():
    yield Client()


@pytest.fixture(scope='module')
def movie_data():
    return {
        'name': 'The Godfather',
        'protagonists': ['Marlon Brando', 'Al Pacino', 'James Caan'],
        'poster': 'https://example.com/poster.jpg',
        'start_date': datetime.utcnow() + timedelta(days=7),
        'status': 'coming-up',
        'ranking': 0,
    }


def test_add_movie(api_client, db, movie_data):
    response = api_client.post('/movies/', data=movie_data)
    assert response.status_code == 200
    assert db.movies.count_documents({}) == 1


def test_add_movie_with_duplicate_name(api_client, db, movie_data):
    db.movies.insert_one(movie_data)
    with pytest.raises(DuplicateKeyError):
        api_client.post('/movies/', data=movie_data)


def test_update_movie(api_client, db, movie_data):
    movie_id = db.movies.insert_one(movie_data).inserted_id
    new_data = {'status': 'running'}
    response = api_client.patch(f'/movies/{str(movie_id)}/', data=new_data)
    assert response.status_code == 200
    assert db.movies.find_one({'_id': ObjectId(movie_id)})['status'] == 'running'


def test_delete_movie(api_client, db, movie_data):
    movie_id = db.movies.insert_one(movie_data).inserted_id
    response = api_client.delete(f'/movies/{str(movie_id)}/')
    assert response.status_code == 204
    assert db.movies.count_documents({}) == 0


def test_ranking_increases(api_client, db, movie_data):
    movie_data['status'] = 'upcoming'
    movie_id = db.movies.insert_one(movie_data).inserted_id
    for i in range(6):
        db.movies.update_one({'_id': movie_id}, {'$inc': {'ranking': 10}})
        response = api_client.get(f'/movies/trending/')
        assert response.status_code == 200
        assert response.json()[0]['_id'] == str(movie_id)


def test_list_trending_movies(api_client, db, movie_data):
    db.movies.insert_one(movie_data)
    response = api_client.get('/movies/trending/')
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['name'] == 'The Godfather'
