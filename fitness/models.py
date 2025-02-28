from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text='In minutes')
    calories_burned = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise} on {self.date}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_value = models.PositiveIntegerField()
    current_value = models.PositiveIntegerField()
    unit = models.CharField(max_length=20)  # e.g., 'kg', 'lbs', 'minutes'
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name