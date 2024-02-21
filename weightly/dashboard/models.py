from django.db import models
from django.contrib.auth.models import User

class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField()

    bmi = models.CharField(default=0, max_length=50, blank=True)  # Domyślna wartość
    suggested_calories = models.FloatField(default=0)  # Domyślna wartość

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg - {self.date}"

