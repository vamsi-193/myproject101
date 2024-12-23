from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def courses(request):
    return render(request, 'courses.html')

def courses_detail(request,data):
    if(data=='python'):
        course_data={'name':'Python Programming','price':'10000','image':'images/python.png'}
    elif(data=='java'):
        course_data={'name':'Java Programming','price':'1000','image':'images/java.png'}
    elif(data=='django'):
        course_data={'name':'Django Framework','price':'5000','image':'images/django.png'}
    elif(data=='uiux'):
        course_data={'name':'UI/UX Design','price':'8000','image':'images/uiux.png'}
    elif(data=='webdevelopment'):
        course_data={'name':'Web Development','price':'6000','image':'images/webdevelopment.png'}
    elif(data=='devops'):
        course_data={'name':'DevOps','price':'7000','image':'images/devops.png'}
    return render(request,'courses_detail.html',course_data)

def bootcamp(request):
    course_data={'name':'6 Months In House Bootcamp Programme','price':'10000','image':'images/bootcamp.png'}
    return render(request,'courses_detail.html',course_data)
