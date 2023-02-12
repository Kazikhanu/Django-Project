from django.db import models

class Kvart(models.Model):
    description = models.TextField(blank=True)
    size = models.CharField(max_length=255)
    prise = models.IntegerField()
    region = models.CharField(max_length=255)
    volume = models.IntegerField()

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Comments(models.Model):
    comment = models.TextField(blank=True)

class Categories(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
class Roles(models.Model ):
    name = models.CharField(max_length=50)





