from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class Project(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=56,blank=False,)
    description=models.CharField(max_length=256,blank=False,)
    published = models.DateField(auto_now_add=True)
    tags=TaggableManager()
    
    def __str__(self):
        return self.name
    

class Collaborator(models.Model):
    
    User=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    description=models.CharField(max_length=256,blank=True)
    tags=TaggableManager()
    medels=models.IntegerField(blank=False,default=0)

    def __str__(self):
        return self.description
    

class Collaboration(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    collaborator=models.ForeignKey(Collaborator,on_delete=models.CASCADE)
    request=models.CharField(max_length=256,blank=False)
    collb_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.project
    

    
        


