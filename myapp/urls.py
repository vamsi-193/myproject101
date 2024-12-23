from django.urls import path
from .views import *
app_name='myapp'

urlpatterns=[
    path('', homepage, name='homepage'),
    path('courses/',courses,name='courses'),    
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('courses/<str:data>/',courses_detail,name='courses_detail'),
]