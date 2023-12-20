from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from .validators import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_auth.models import CourseCreatorProfile,CourseUserProfile
from home.validators import get_user_type
# Create your views here.
def sign_up(request):
    
    if request.method=="POST":
        username=request.POST["username"]
        pass_1=request.POST["pass-1"]
        pass_2=request.POST["pass-2"]
        email=request.POST["email"]
        
        is_student=request.POST.get("student",None)
        is_creator=request.POST.get("creator",None)
        
        
        
        is_password_valid,error_type =validator_password(pass_1,pass_2)
        
#----------------------VALIDATORS------------------------------
        #passowrd validation
        if(not is_password_valid):
            messages.error(request,error_type)
            return HttpResponseRedirect('/auth/sign-up/')
        if(is_student==None and is_creator==None):
            messages.error(request,"please select any single profession")
            return HttpResponseRedirect('/auth/sign-up/')
        if(is_student and is_creator):
                messages.error(request,"please select any single profession")
                return HttpResponseRedirect('/auth/sign-up/')
        
        
        # check user allready exist or not
        if_email_exists=User.objects.filter(email=email)
        if_username_exists=User.objects.filter(username=username)
       
        if((if_username_exists.count()!=0) or (if_email_exists.count()!=0)):
            messages.error(request,"user  Allready exists")
            return HttpResponseRedirect('/auth/sign-up/')
        
        user=User.objects.create(username=username,email=email,password=pass_1)
       
        user.save()
       
        #creating profile for the user
        if(is_student):
            create_profile(user,"student")
        if(is_creator):
            create_profile(user,"creator")
   
        messages.success(request,"account created successfully !!!")
        return HttpResponseRedirect('/auth/sign-in/')
        

    return render(request,"signup.html")

def sign_in(request):
   
    # i will create sign in using sesions creation
    if (request.method=="POST"):
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user=User.objects.get(username=username,password=password)
            
            if user:
                login(request,user)
                print(request.user)
                return HttpResponseRedirect('/home/')
        
        except:
            messages.error(request,"user does not exists")
            return HttpResponseRedirect('/auth/sign-up/')
        

        
        
    
    
    return render(request,"signin.html")


@login_required(login_url='/auth/sign-in')
def log_out(request):
    logout(request)
    messages.success(request,"Logged out successfully !!")
    return HttpResponseRedirect('/auth/sign-in/')




def update_profile(request,username):
    
    if request.user.username!=username: return HttpResponse("permission denied")
    
    #getting the type of user
    user_type,user_object=get_user_type(request)
    user_profile=user_object
    
 
    if request.method=="POST":
        full_name=request.POST["full_name"]
        college_name=request.POST["college_name"]
        github_id=request.POST["github_id"]
        sex=request.POST["sex"]
        linkedin_id=request.POST["linkedin_id"]
        
        if(user_type=="creator"):
            creator_profile=user_object
            creator_profile.full_name=full_name or  creator_profile.full_name
            creator_profile.sex=sex or creator_profile.sex
            creator_profile.github_id=github_id or  creator_profile.github_id
            creator_profile.college_name=college_name or creator_profile.college_name
            creator_profile.linkedin_id=linkedin_id or creator_profile.linkedin_id
            creator_profile.save()
            print("saved")
            
        elif(user_type=="student"):
            student_profile=user_object
            student_profile.full_name=full_name or  student_profile.full_name
            student_profile.sex=sex or  student_profile.sex
            student_profile.github_id=github_id or  student_profile.github_id
            student_profile.linkedin_id=linkedin_id or student_profile.linkedin_id
            student_profile.college_name=college_name or  student_profile.college_namor 
            student_profile.save()
            print("saved")
        return HttpResponseRedirect(f'/auth/{username}/update-profile')
        
    context={"user_profile":user_profile,"user_type":user_type}
    return render(request,"user-profile-settings.html",context)
    









    
def error_page(request):
    return render(request,'404.html')

