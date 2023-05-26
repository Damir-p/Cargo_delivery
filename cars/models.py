from django.db import models
import random, string
from django.core.validators import MinValueValidator, MaxValueValidator
from location.models import Location


def generate_random_letter():
    return random.choice(string.ascii_uppercase)


class Car(models.Model):
    unique_number = models.CharField(
        max_length=5, 
        unique=True
        )
    current_location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE)
    carrying_capacity = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(1000)
            ]
        )

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
    
    def __str__(self):
        return self.unique_number


    def save(self, *args, **kwargs):
        if not self.unique_number:
            self.unique_number = f"{random.randint(1000, 9999)}{generate_random_letter()}"
            locations = Location.objects.all()
        
        if not self.current_location:
            random_location = random.choice(locations)
            self.current_location = random_location
        super().save(*args, **kwargs)


        