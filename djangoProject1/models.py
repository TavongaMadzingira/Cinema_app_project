from django.db import models


class Movie(models.Model):
    id = None
    name = models.CharField(max_length=255)
    protagonists = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    start_date = models.DateField()
    STATUS_CHOICES = (
        ('coming-up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coming-up')
    ranking = models.IntegerField(default=0)
