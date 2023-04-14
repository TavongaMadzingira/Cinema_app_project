import boto3
from django.db import models
from django.utils import timezone

s3 = boto3.resource('s3')
bucket_name = 'your-s3-bucket-name'

class Movie(models.Model):
    # Fields for movie data
    name = models.CharField(max_length=255)
    protagonists = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=COMING_UP)
    ranking = models.IntegerField(null=True, blank=True)

    # Field for storing image URL in S3
    image_url = models.URLField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if an image was uploaded
        if self.image:
            # Generate a unique filename for the image based on the movie name
            filename = f"{self.name}_{timezone.now().strftime('%Y%m%d%H%M%S%f')}.jpg"

            # Upload the image to S3
            s3.Object(bucket_name, filename).put(Body=self.image.read(), ContentType='image/jpeg')

            # Set the image URL field to the S3 URL
            self.image_url = f"https://{bucket_name}.s3.amazonaws.com/{filename}"

            # Delete the local image file
            self.image.delete()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image from S3 if it exists
        if self.image_url:
            filename = self.image_url.split('/')[-1]
            s3.Object(bucket_name, filename).delete()

        super().delete(*args, **kwargs)
