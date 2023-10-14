from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Course,Student,Faculty,FacultyCourseMapping
from .forms import AddFacultyForm,AddStudentForm,UpdateFacultyForm


def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})

def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
        print(flag)
        if flag:
            print("login success")
            request.session["auname"]=adminuname
            return render(request,"adminhome.html",{"adminuname":adminuname})
        else:
            message="enter valid credentials"
            return render(request,"login.html",{"msg":message})



def viewstudents(request):
    auname = request.session["auname"]
    students=Student.objects.all()
    count=Student.objects.count()
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname":auname})
def viewcourses(request):
    auname = request.session["auname"]
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursesdata":courses,"count":count,"adminuname":auname})
def viewfaculty(request):
    auname = request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})
def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})
def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})
def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})
def addcourse(request):
    auname = request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})
def insertcourse(request):
    auname = request.session["auname"]
    dept=request.POST["dept"]
    program=request.POST["program"]
    ay=request.POST["ay"]
    sem=request.POST["sem"]
    year=request.POST["year"]
    ccode=request.POST["ccode"]
    ctitle=request.POST["ctitle"]
    ltps=request.POST["ltps"]
    credits=request.POST["credits"]
    course=Course(department=dept,program=program,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
    Course.save(course)
    message="course added successfully"
    return render(request,"addcourse.html",{"msg":message,"adminuname":auname})
def updatecourse(request):
    auname=request.session["auname"]
    courses=Course.objects.all()
    count=Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"count":count,"courses":courses})
def courseupdation(request,cid):
    auname=request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})
def courseupdated(request):
    auname=request.session["auname"]
    cid=request.POST["cid"]
    ctitle=request.POST["ctitle"]
    ltps=request.POST["ltps"]
    credits=request.POST["credits"]
    Course.objects.filter(Q(id=cid)).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    message="updated successfully"
    return render(request,"courseupdation.html",{"adminuname":auname,"msg":message})
def deletecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "deletecourse.html", {"coursesdata": courses, "count": count,"adminuname":auname})
def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")
def addfaculty(request):
    auname = request.session["auname"]
    form=AddFacultyForm()
    if request.method=="POST":
        form1= AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="faculty added successfully"
            return render(request,"addfaculty.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message = "failed to add faculty"
            return render(request, "addfaculty.html", {"msg": message, "form": form,"adminuname":auname})
    return render(request,"addfaculty.html",{"form":form,"adminuname":auname})
def updatefaculty(request):
    auname=request.session["auname"]
    facultys=Faculty.objects.all()
    count=Faculty.objects.count()
    return render(request,"updatefaculty.html",{"adminuname":auname,"count":count,"facultys":facultys})
def facultyupdation(request,fid):
    auname=request.session["auname"]
    faculty=Faculty.objects.get(Q(id=fid))
    form=UpdateFacultyForm(instance=faculty)
    if request.method=="POST":
        form1=UpdateFacultyForm(request.POST,instance=faculty)
        if form1.is_valid():
            form1.save()
            message="updated successfully"
            return render(request,"facultyupdation.html",{"form":form,"msg":message,"adminuname":auname})
        else:
            message = "update unsuccessful"
            return render(request, "facultyupdation.html", {"form": form, "msg": message,"adminuname":auname})

    return render(request,"facultyupdation.html",{"form":form,"adminuname":auname})

def deletefaculty(request):
    auname = request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})
def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")

def addstudent(request):
    auname = request.session["auname"]
    form=AddStudentForm()
    if request.method=="POST":
        form1= AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="student added successfully"
            return render(request,"addstudent.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message="failed to add student"
            return render(request, "addstudent.html", {"msg": message, "form": form, "adminuname": auname})
    return render(request,"addstudent.html",{"form":form,"adminuname":auname})

def deletestudent(request):
    auname = request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentdata": student, "count": count,"adminuname":auname})
def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")
def updatestudent(request):
    auname=request.session["auname"]
    students=Student.objects.all()
    count=Student.objects.count()
    return render(request,"updatestudent.html",{"adminuname":auname,"count":count,"students":students})
def studentupdation(request,sid):
    auname=request.session["auname"]
    return render(request,"studentupdation.html",{"sid":sid,"adminuname":auname})
def studentupdated(request):
    auname = request.session["auname"]
    sid=request.POST["sid"]
    dept=request.POST["dept"]
    program=request.POST["program"]
    year=request.POST["year"]
    sem=request.POST["sem"]
    email=request.POST["email"]
    contact=request.POST["contact"]
    Student.objects.filter(Q(id=sid)).update(department=dept,program=program,year=year,semester=sem,email=email,contact=contact)
    message="updated successfully"
    return render(request,"studentupdation.html",{"adminuname":auname,"msg":message})
def facultycoursemapping(request):
    auname = request.session["auname"]
    fmcourses=FacultyCourseMapping.objects.all()
    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses})
def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})
def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        Admin.objects.filter(username=auname).update(password=npwd)
        message="password updated successfully"
        return render(request,"adminchangepwd.html",{"adminuname":auname,"msg":message})
    else:
        print("old password is wrong")
        message = "update unsuccessful"
        return render(request, "adminchangepwd.html", {"adminuname": auname, "msg": message})

