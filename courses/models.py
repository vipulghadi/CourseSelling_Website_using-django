from django.db import models

# Create your models here.
from django.db import models
import uuid
from user_auth.models import CourseCreatorProfile,CourseUserProfile

class Course(models.Model):
    
    course_name=models.CharField(max_length=100,null=False)
    course_slug=models.CharField(max_length=100,unique=True,null=False,primary_key=True)
    course_desc=models.CharField(max_length=200,null=False)
    course_price=models.DecimalField(max_digits=10,decimal_places=2,null=False,default=0.0)
    course_discount=models.IntegerField(default=0)
    course_status=models.BooleanField(default=False)
    # course_thumbnail=models.ImageField(null=True,upload_to="files/thumbnails")
    course_create_date=models.DateTimeField(auto_now_add=True)
    course_length=models.DecimalField(null=False,decimal_places=2,max_digits=10)
    course_creator=models.ForeignKey(to=CourseCreatorProfile,on_delete=models.CASCADE)
    course_rating=models.PositiveIntegerField(default=0,null=True,blank=True)
    course_user_count=models.PositiveIntegerField(default=0,null=True,blank=True)
    course_tags=models.CharField(max_length=200,default="course")
    
    def __str__(self):
        return self.course_name
    
# class Tags(models.Model):
#     desc=models.CharField(max_length=50,null=False)
#     course=models.ForeignKey(to=Course,related_name="tag",on_delete=models.CASCADE)
#     def __str__(self):
#         return self.desc
    
# class Prerequisite(models.Model):
#     desc=models.CharField(max_length=50,null=False)
#     course=models.ForeignKey(to=Course,related_name="pre",on_delete=models.CASCADE)
#     def __str__(self):
#         return self.desc
    
# class Learnings(models.Model):
#     desc=models.CharField(max_length=100,null=False)
#     course=models.ForeignKey(to=Course,related_name="learning",on_delete=models.CASCADE)
#     def __str__(self):
#         return self.desc
    
 



class VideoLecture(models.Model):
    
    title=models.CharField(max_length=100,null=False)
    course=models.ForeignKey(to=Course,related_name="videos",on_delete=models.CASCADE)
    # video_thumbnail=models.ImageField(upload_to="lecture-thumbnails")
    serial_number=models.IntegerField(null=False,default=1)
    video_url_id=models.CharField(max_length=50,null=False)
    is_preview=models.BooleanField(default=False)
    def __str__(self):
        return self.title
 
 
  
 

#details about the course taken by Student

class UserCourseDetails(models.Model):
    user=models.ForeignKey(to=CourseUserProfile,on_delete=models.CASCADE)
    course=models.ForeignKey(to=Course,on_delete=models.CASCADE)
    buy_date=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    status=models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return f'{self.user.full_name}:{self.course.course_name}'

class UserVideoStatus(models.Model):
    user=models.ForeignKey(to=CourseUserProfile,on_delete=models.CASCADE)
    course=models.ForeignKey(to=Course,on_delete=models.CASCADE)
    video=models.ForeignKey(to=VideoLecture,on_delete=models.CASCADE)
    is_watched=models.BooleanField(default=False)
    
    