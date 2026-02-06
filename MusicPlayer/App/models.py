from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    image_file = models.ImageField(upload_to='image_file/', blank=True, null=True)
    audio_file = models.FileField(upload_to='audio_file/', blank=True, null=True)
    audio_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
