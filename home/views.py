from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from courses.models import CourseCreatorProfile,CourseUserProfile
from .validators import *
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        user_type,user_object=get_user_type(request)
        
       
        
        context={"user_type":user_type}
        return render(request,"homepage.html",context)
    else: 
        return HttpResponseRedirect('/auth/sign-in/')



def aboutpage(request):
    user_type=get_user_type(request)[0]
    return render(request,"my-about.html",{"user_type":user_type})



