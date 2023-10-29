from django.db import models
from base.models import *

class Projects(BaseModel):
  title = models.CharField(max_length=100)
  desc = models.CharField(max_length=200)
  full_desc = models.CharField(max_length=500)
  image = models.ImageField(upload_to='project_image/')
  prev_url = models.CharField(max_length=100)
  price = models.IntegerField()
  contact = models.IntegerField()