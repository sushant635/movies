from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    movie_titel = models.CharField(max_length=300,null=True,blank=True)
    movie_description = models.CharField(max_length=500,null=True,blank=True)
    movie_genres = models.CharField(max_length=200,null=True,blank=True)
    uuid = models.CharField(max_length=100,null=True,blank=True,unique=True)

    def __str__(self):
        return self.title
