from django.db import models
from base.models import BaseModel
# Create your models here.
class UserProfile(BaseModel):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  college = models.CharField(max_length=200)
  role = models.CharField(max_length=100,blank=True,null=True)
  mobile = models.CharField(max_length=20,blank=True,null=True)
  email = models.EmailField(unique=True)
  job_completed = models.IntegerField(default=0)
  earn = models.IntegerField(default=0)
  ontime = models.IntegerField(default=0)
  bio = models.CharField(max_length=300,blank=True)
  address = models.CharField(max_length=200,blank=True,null=True)
  socials = models.CharField(max_length=200,blank=True,null=True)
  pow = models.CharField(max_length=200,blank=True,null=True)


  def __str__(self):
    return self.email


class lancer(BaseModel):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  company = models.CharField(max_length=200,blank=True,null=True)
  role = models.CharField(max_length=100,blank=True,null=True)
  skills = models.CharField(max_length=100,blank=True,null=True)
  email = models.EmailField(unique=True)
  phone = models.IntegerField(blank=True,null=True)
  bio = models.CharField(max_length=100,blank=True,null=True)
  socials = models.CharField(max_length=100, null=True)
  job_provided = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.email