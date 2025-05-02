from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AgriculturalCulture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ripening_time = models.IntegerField()
    planted_area = models.DecimalField(max_digits=10, decimal_places=2)
    planting_date = models.DateField()
    field_number = models.IntegerField()

    class Meta:
        ordering = ['-planting_date']
        indexes = [
            models.Index(fields=['planting_date']),
        ]

    def __str__(self):
        return self.title
