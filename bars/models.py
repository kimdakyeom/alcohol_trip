from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    grade = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )
    

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    hours = models.TimeField()
    parking = models.BooleanField()
    contact = models.CharField(max_length=30)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )


class Comment(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
