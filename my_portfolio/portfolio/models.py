from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    technologies = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
    