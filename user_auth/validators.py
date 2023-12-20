from  user_auth.models import CourseCreatorProfile,CourseUserProfile


#password validation
def validator_password(p1,p2):
    error=None
    if p1==p2:
        if(len(p1)<6):
            error="password size must be greater then 5"
            return [False,error]
        else: return [True,error]
       
    elif(p1!=p2):
        error="password not matching"
        return [False,error]


#function to create user profile
def create_profile(user,profession):
    
    
    if profession=="student":
        CourseUserProfile.objects.create(user=user,i_am="student").save()
    
    elif profession=="creator":
        CourseCreatorProfile.objects.create(user=user,i_am="creator").save()
    
    