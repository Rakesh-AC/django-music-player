from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.PositiveIntegerField()
    file = models.FileField(upload_to='songs/')


    def __str__(self):
        return self.title
    

