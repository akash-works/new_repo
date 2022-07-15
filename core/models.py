from email.headerregistry import Address
from importlib.resources import contents
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=400)
    contents=models.TextField(blank=True)
    # age=models.PositiveIntegerField(blank=True,null=True)
    # Address=models.CharField(max_length=500)

class Email(models.Model):
    title=models.CharField(max_length=500)
    contents=models.TextField(blank=True)

class Hvs(models.Model):
    student_name=models.CharField(max_length=100)
    contents=models.TextField(blank=True)


