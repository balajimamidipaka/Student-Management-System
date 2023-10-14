from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from adminapp.models import Student,Course
from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    sid=request.session["sid"]
    student=Student.objects.get(studentid=sid)
    return render(request,"studenthome.html",{"sid":sid,"student":student})
def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]
    flag = Student.objects.filter(Q(studentid=sid) & Q(password=pwd))
    print(flag)
    if flag:
        print("login success")
        request.session["sid"] = sid
        student = Student.objects.get(studentid=sid)
        return render(request, "studenthome.html", {"sid": sid,"student":student})
    else:
        message = "enter valid credentials"
        return render(request, "studentlogin.html", {"msg": message})

def studentchangepwd(request):
    sid=request.session["sid"]
    return render(request,"studentchangepwd.html",{"sid":sid})
def studentupdatepwd(request):
    sid=request.session["sid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        Student.objects.filter(studentid=sid).update(password=npwd)
        message="password updated successfully"
        return render(request,"studentchangepwd.html",{"sid":sid,"msg":message})
    else:
        message = "update unsuccessful"
        return render(request, "studentchangepwd.html", {"sid": sid, "msg": message})
def studentcourses(request):
    sid=request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})
def displaystudentcourses(request):
    sid=request.session["sid"]
    ay=request.POST["ay"]
    sem=request.POST["sem"]
    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))
    if len(courses)==0:
        message="no courses found"
        return render(request,"studentcourses.html",{"msg":message,"sid":sid})
    else:
        return render(request,"displaystudentcourses.html",{"sid":sid,"courses":courses})
def studentcoursecontent(request):
    sid=request.session["sid"]
    content=CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})
