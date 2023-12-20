from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import uuid 
from django.contrib.auth.backends import BaseBackend

from courses.models import *


class CourseCreatorProfile(models.Model):

    STATUS_CHOICES = (
    ("M", ("Male")),
    ("F", ("Female")),
    
)  
    user=models.OneToOneField(to=User,on_delete=models.CASCADE ,related_name="course_creator")
    i_am=models.CharField(max_length=100,default="")
    creator_id=models.UUIDField(default=uuid.uuid4())
    full_name=models.CharField(max_length=100,null=True,default="")
    sex=models.CharField(choices=STATUS_CHOICES,null=False,max_length=1)
    college_name=models.CharField(max_length=100,null=True,default="")
    linkedin_id=models.URLField(null=True,default="")
    github_id=models.URLField(null=True,default="")
    social_id=models.URLField(null=True,default="")
    
    def __str__(self):
        return f'course_creator:{self.full_name}'

class CourseUserProfile(models.Model):
    STATUS_CHOICES = (
    ("M", ("Male")),
    ("F", ("Female")),
)   
    
    i_am=models.CharField(max_length=100,default="")
    user=models.OneToOneField(to=User,on_delete=models.CASCADE,related_name="course_user")
    student_id=models.UUIDField(default=uuid.uuid4(),primary_key=True,unique=True)
    full_name=models.CharField(max_length=100)
    sex=models.CharField(choices=STATUS_CHOICES,null=False,max_length=1)
    college_name=models.CharField(max_length=100,null=True,default="")
    linkedin_id=models.URLField(null=True,default="")
    github_id=models.URLField(null=True,default="")
    social_id=models.URLField(null=True,default="")
    
    def __str__(self):
        return f'student:{self.full_name}'
    
    
