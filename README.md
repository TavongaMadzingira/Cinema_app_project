Cinema app


This is a cinema app implemented in Python using Postgres, MongoDB, Celery, Redis, RabbitMQ, and Django Ninja. 
The program allows users to add new movies via an API, with each movie having a name, list of protagonists, poster image, start date, status, and ranking field.
It also synchronizes Postgres movie instances to MongoDB, accounts for all cases (creation, deletion, etc.), and increases the rank of each instance by 10, once every 5 minutes, from the movie creation (status=upcoming) to the movie launch (status=running).

Finally, it provides an API to list sorted trending movies from MongoDB.

Files/Description

celery.py: This file contains the Celery instance and configuration for our project. We have used Redis as the broker and backend for Celery. We have also set up periodic tasks for updating the movie rankings.

settings.py: This is the main Django settings file where we have added the necessary configuration for using Postgres, MongoDB, and Celery. We have also added configuration for RabbitMQ to be used with Celery. Additionally, we have included Django Ninja and configured it to use JSON Web Tokens (JWT) for authentication.

urls.py: This file contains the main URL configuration for our Django project. We have included the URLs for the Django admin panel, the Django Ninja API endpoints, and the Celery Flower monitoring tool.

models.py: This file contains the Django models for our cinema program. We have defined a Movie model that has fields for name, protagonists, poster, start_date, status, and ranking. We have used the django-mongodb-engine package to sync the Movie instances between Postgres and MongoDB.

views.py: This file contains the Django views for our cinema program. We have defined API views for creating, updating, deleting, and listing movies. We have also added a view for listing trending movies based on their rankings.

tasks.py: This file contains the Celery tasks for updating the movie rankings. We have defined a task that runs every 5 minutes and updates the ranking of movies that are in the "upcoming" or "starting" status.

Docker-compose.yml: This file specifies all dependencies such as the environment, broker and database URL.

Suggested Improvements ;)

Use a dedicated image storage service like Amazon S3 to store posters for films (see file entitled S3.py for code implementation).
