from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.TextField(max_length=20)
    name = models.TextField(max_length=20)
   
    
    
class Subject(models.Model):
    title = models.TextField(max_length=50)
    Q = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    code = models.TextField(max_length=30)
    user = models.ManyToManyField(User)
    
class Reputation(models.Model):
    subject = models.ForeignKey(Subject)
    content = models.TextFirld(max_length=200)
    user = models.OneToOneField(User)
    goodcount = models.IntegerField(default=0)
    