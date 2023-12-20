

from django.urls import path,include
from user_auth.views import *

urlpatterns = [
    path("sign-up/",sign_up),
    path("sign-in/",sign_in),
    path("log-out/",log_out),
    path("<username>/update-profile/",update_profile ,name="update_profile"),
    path("something-went-wrong/",error_page),
    
]

