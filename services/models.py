from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    first_visited_date = models.DateField()
    rank = models.IntegerField()