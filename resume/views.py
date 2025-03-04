from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")

def projects (request):
    projects_show=[
        {
            'title': 'Ice Cream Shop POS System',
            'path': 'images/Ice Cream Shop POS.jpg',
        },
        {
            'title': 'Django Space Game',
            'path': 'images/python space game.jpeg',
        },
        {
            'title': 'Heartdroid',
            'path': 'images/heartdroid.jpeg',
        },
        {
            'title': 'Portfolio',
            'path': 'images/Dashboard .png',
        },
    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience=[
        {"company":"ABC",
         "position":"python developer"},
        {"company":"ABC2",
         "position":"python developer2"},
        {"company":"ABC3",
         "position":"python developer3"}
    ]
    return render (request,"experience.html",{"experience":experience})

def certificate(request):
    return render (request, "certificate.html")

def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resumekennetheladistu.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resumekennetheladistu.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
