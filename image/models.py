from django.db import models
# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length = 50)
    city = models.CharField(max_length = 90)
    
    def __str__(self):
        return self.country, +'/'+ self.city


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 90)

    def __str__(self):
        return self.name

class Image(models.Model):

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=244)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name