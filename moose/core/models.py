from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=64)

class EmailRecord(models.Model):
    user = models.ForeignKey(User)
    gmailuuid = models.IntegerField()
    fromaddress = models.CharField(max_length=150)
    body_text = models.TextField()
    company = models.ForeignKey(Company)

class Favorite(models.Model):
    email = models.IntegerField()
    isFavorite = models.BooleanField()
