from django.db import models


class Covers(models.Model):
    username = models.CharField(max_length=50)
    cover_title = models.CharField(max_length=100)
    cover_artist = models.CharField(max_length=100)
    cover_song = models.CharField(max_length=100)
    cover_genre = models.CharField(max_length=50, default='Cover')
    audio_url = models.CharField(max_length=150, default="")

    def __str__(self):
        return f'{self.username}, {self.cover_title}, {self.cover_song}'