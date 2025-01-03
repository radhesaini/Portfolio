# models.py
from django.db import models

class HomePage(models.Model):
    heading = models.CharField(max_length=255)
    subheading = models.TextField(blank=True, null=True)
    carousel_images = models.ManyToManyField('CarouselImage', blank=True) 

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')

class JourneyHighlight(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # e.g., "fa-code", "fa-briefcase"
