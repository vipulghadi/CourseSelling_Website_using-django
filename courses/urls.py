

from django.urls import path,include
from user_auth.views import *
from courses.views import *
urlpatterns = [
    path("",display_all_courses,name="courses"),
    path("create-course/",create_course,name="create-course"),
    path("<creator>/<course_slug>/add-lectures/",create_lectures_for_course),
    path("<user>/all-courses/",display_creator_courses,name="display_creator_courses"),
    path("<course_slug>/<id>/delete/",delete_lecture_video,name="delete lecture"),
    path("<username>/",display_user_enroll_course,name="display_user_enroll_courses"),
    path("buy-course/<username>/<course_slug>/",buy_course,name="buy_course"),
]
