from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     activity_type = models.CharField(max_length=100)
#     duration = models.DurationField()
#     distance = models.FloatField()
#     calories_burned = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)

# class Goal(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     goal_type = models.CharField(max_length=100)
#     target_value = models.FloatField()
#     achieved = models.BooleanField(default=False)

class Exercise(models.Model):
    name=models.CharField(max_length=30,null=True)
    description=models.TextField(null=True)

class Asana(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='asanas')
    is_completed = models.BooleanField(default=False)
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)


class Progress(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)  # e.g., "In Progress", "Completed"
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2)


class UserExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)