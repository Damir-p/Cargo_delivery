from django.db import models

class Location(models.Model):
    city = models.CharField(
        max_length=100
        )
    state = models.CharField(
        max_length=100
        )
    postcode = models.CharField(
        max_length=20
        )
    latitude = models.FloatField(
        null=False, 
        default=0.0
        )
    longitude = models.FloatField(
        null=False, 
        default=0.0
        )

    class Meta:
        verbose_name = "Locations"
        verbose_name_plural = "Locations"
    
    def __str__(self):
        return f"{self.city}, {self.state} {self.zip_code}"