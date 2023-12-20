from courses.models import CourseCreatorProfile,CourseUserProfile

def get_user_type(request): 
    try:
        student=CourseUserProfile.objects.get(user=request.user)
        return ["student",student]
    except:
        creator=CourseCreatorProfile.objects.get(user=request.user)
        return ["creator",creator]
    
    