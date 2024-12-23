from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    name=models.CharField(max_length=300)
