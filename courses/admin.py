from django.contrib import admin
from courses.models import *
# Register your models here.


# class TagsAdmin(admin.TabularInline):
#     model=Tags

# class LearningsAdmin(admin.TabularInline):
#     model=Learnings
    
# class PreAdmin(admin.TabularInline):
#     model=Prerequisite

class VideoAdmin(admin.TabularInline):
    model=VideoLecture


class CourseAdmin(admin.ModelAdmin):...
   
admin.site.register(Course,CourseAdmin)
admin.site.register(CourseCreatorProfile)
admin.site.register(CourseUserProfile)
admin.site.register(UserCourseDetails)
        
