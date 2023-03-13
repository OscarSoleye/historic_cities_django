from django.db import models
from django.conf import settings

# Create your models here.
class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.TextField()
    otherName = models.TextField()
    country = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    year = models.TextField()
    pop = models.TextField()
    city_id = models.TextField()

    def __str__(self):
        return f'{self.id}, {self.city}, {self.otherName}, {self.country}, {self.latitude}, {self.longitude}, {self.year}, {self.pop}, {self.city_id}'
