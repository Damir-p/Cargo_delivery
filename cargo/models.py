from django.db import models
from location.models import Location

class Cargo(models.Model):
    pick_up_location = models.ForeignKey(
        Location, 
        related_name='pick_up_cargos', 
        on_delete=models.CASCADE
        )
    delivery_location = models.ForeignKey(
        Location, 
        related_name='delivery_cargos', 
        on_delete=models.CASCADE)
    weight = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    
    def __str__(self):
        return f"Cargo #{self.pk}"
    
    