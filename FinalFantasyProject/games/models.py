from django.db import models

# Create your models here.


from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField("release date")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    jobs = models.ForeignKey('Job', on_delete=models.CASCADE)
    character_description = models.TextField()
    def __str__(self):
        return self.name

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    def __str__(self):
        return self.genre_name

class Job(models.Model):
    job_name = models.CharField(max_length=50)
    job_description = models.TextField()
    def __str__(self):
        return self.job_name







