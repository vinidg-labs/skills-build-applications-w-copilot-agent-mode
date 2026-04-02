from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_id = models.CharField(max_length=100)  # Armazena o id do usuário como string
    user_name = models.CharField(max_length=100)  # Redundância para facilitar queries
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user_name} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    points = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.user_name} - {self.rank}"
