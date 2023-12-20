from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from user_auth.models import CourseCreatorProfile,CourseUserProfile
from courses.models import Course,VideoLecture,UserCourseDetails
from django.contrib import messages
from home.validators import get_user_type
# Create your views here.



#display all courses in our server
# also highlight student enrolled courses

def display_all_courses(request):
    
    user_type,user_object=get_user_type(request)
    student_courses=None
    #handling user courses
    if user_type=="student":
        student_courses=UserCourseDetails.objects.filter(user=user_object)
        
    print(user_type)
    courses=Course.objects.all()
    
    context={"courses":courses,"user_type":user_type}
    return render(request,"courses.html",context)


# this function is for creating a new course and by creator
def create_course(request):
    #-------note: we have to add custome validation for this
    user_type=get_user_type(request)[0]
    if (request.method=="POST"):
        
        creator=CourseCreatorProfile.objects.get(user=request.user)
        course_name=request.POST["course_name"]
        course_slug=request.POST["course_slug"]
        course_thumbnail=request.FILES
        course_desc=request.POST["course_desc"]
        course_price=request.POST["course_price"]
        course_discount=request.POST["course_discount"]
        course_status=request.POST["course_status"]
        course_length=request.POST["course_length"]
        tags=request.POST["tags"]
        course_creator=creator
        
        Course.objects.create(
        course_name=course_name,course_slug=course_slug,
        course_desc=course_desc,course_price=course_price,
        course_discount=course_discount,course_status=course_status,
        # course_thumbnail=course_thumbnail,
        course_length=course_length,
        course_creator=creator,course_tags=tags,).save()
        
        return HttpResponseRedirect(f'/courses/{request.user.username}/{course_slug}/add-lectures/')
    context={"user_type":user_type}
    return render(request,'create-course.html',context)


# this function is for creating the lectures for the course as well as updating purpose
def create_lectures_for_course(request,creator,course_slug):
    # if some other user try to access this page ,permission will denied
    if str(request.user.username)!=creator:
        return HttpResponse("permission denied")
    
    #getting course 
    course=Course.objects.get(course_slug=course_slug)
    lectures=None
    
    if request.method=="POST":
        #must add validators for uniqueness of video
        try:  
            video_title=request.POST["video_title"]
            video_url=request.POST["video_url"]
            video_is_preview=bool(request.POST["video_is_preview"])
            lecture=VideoLecture.objects.create(
              
                                                title=video_title,course=course,
                                                serial_number=1,video_url_id=video_url,
                                                is_preview=video_is_preview)
            lecture.save()
            print("added")
            messages.success(request,"lecture added!")
            
            return HttpResponseRedirect (f'/courses/{creator}/{course_slug}/add-lectures/')
        
        except Exception as e:
            
            print("error")
            messages.error(request,e)
            
    if request.method=="GET":
        # if method is get we will display lectures of the given course if exists
        
        lectures=VideoLecture.objects.filter(course=course)
        
        
    
    context={"username":request.user.username,
             "course_name":course_slug,"lectures":lectures,
             "user_type":"creator"}
    
    return render(request,'add-course-video.html',context)


def delete_lecture_video(request,course_slug,id):
    # if an another user try to delete this video we have to redirect him to home page
    creater=Course.objects.get(course_slug=course_slug).course_creator.user.username
    
    
    if(creater!= request.user.username) :HttpResponseRedirect("/home/")
    try:
        VideoLecture.objects.get(id=id).delete()
        messages.success(request,"video deleted")
        return HttpResponseRedirect(f'/courses/{request.user.username}/{course_slug}/add-lectures/')
        return 
    except:
        return HttpResponseRedirect(f'/courses/{request.user.username}/{course_slug}/add-lectures/')
         

# display all enrolled courses of user
def display_user_enroll_course(request,username):
    user_type,user_object=get_user_type(request)
    student_courses=UserCourseDetails.objects.filter(user=user_object)
    
    print(student_courses)
    return render(request,"user-enroll-courses.html")


#display all courses created by creator
def display_creator_courses(request,user):
    if(str(request.user)!= user):return HttpResponseRedirect('/home/')
    # get all courses created by user
    creator_courses=Course.objects.filter(course_creator=request.user.course_creator)
    context={"courses":creator_courses,"user_type":"creator"}
    return render(request,'creator-all-courses.html',context)



#tempory logic to buy course
def buy_course(request,username,course_slug):
    user_type,user_object=get_user_type(request)
    if user_type=="creator": return HttpResponse("permission denied!")
    
    course=Course.objects.get(course_slug=course_slug)
    UserCourseDetails.objects.create(user=user_object,course=course,is_paid=True).save()
    
    return HttpResponseRedirect('/courses/')
    
    
    
    
