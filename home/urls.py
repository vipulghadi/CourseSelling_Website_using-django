

from django.urls import path,include
from user_auth.views import *
from home.views import *

urlpatterns = [
    path("",homepage,name="home"),
    
    
]

