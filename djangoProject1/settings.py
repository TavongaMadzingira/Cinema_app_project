DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_NAME = 'mydatabase'

CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ''
    'movies',
    ''
    'django_celery_results',
    ''
    'django_celery_beat',
    ''
    'django_mongodb_engine',
    ''
    'djangoninja'
]

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'

CELERY_BEAT_SCHEDULE = {
    'update_movie_ranking': {
        'task': 'movies.tasks.update_movie_ranking',
        'schedule': 300,  # 5 minutes
    },
}


def get_db():
    return None