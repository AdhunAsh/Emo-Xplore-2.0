from django.db import models

# Create your models here.
class Place(models.Model) :
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/' , default=None)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)

class Image(models.Model) :
    images = models.ManyToManyField(Place , related_name= 'images')
       
class Category(models.Model) :
    Name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="images/" , default = None)
    places =models.ManyToManyField(Place , related_name= 'categories')
    
class Emotion(models.Model) :
    emotion = models.CharField(max_length=30)
    message = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category , related_name= 'emotions')
    