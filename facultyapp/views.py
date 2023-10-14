from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from adminapp.models import Faculty,FacultyCourseMapping,Course

from .forms import AddContentForm


# Create your views here.
def facultyhome(request):
    fid=request.session["fid"]
    faculty=Faculty.objects.get(facultyid=fid)
    print(faculty)
    return render(request,"facultyhome.html",{"fid":fid,"faculty":faculty})

def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]
    faculty = Faculty.objects.get(facultyid=fid)
    flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=pwd))
    print(flag)
    if flag:
        print("login success")
        request.session["fid"] = fid
        return render(request, "facultyhome.html", {"fid": fid,"faculty":faculty})
    else:
        message = "enter valid credentials"
        return render(request, "facultylogin.html", {"msg": message})

def facultycourses(request):
    fid=request.session['fid']
    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        if course.faculty.facultyid==int(fid):
            fmcourses.append(course)
    count = len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})
def facultyaddcontent(request):
    fid=request.session["fid"]
    form=AddContentForm()
    if request.method=="POST":
        form1=AddContentForm(request.POST)
        if form1.is_valid():
             form1.save()
             message="content added successfully"
             return render(request,"facultyaddcontent.html",{"fid":fid,"form":form,"msg":message})
        # else:
        #     message = "not able to add content"
        #     return render(request, "facultyaddcontent.html", {"fid": fid, "form": form, "msg": message})
    return render(request,"facultyaddcontent.html",{"fid":fid,"form":form})


def facultychangepwd(request):
    fid=request.session["fid"]
    return render(request,"facultychangepwd.html",{"fid":fid})
def facultyupdatepwd(request):
    fid=request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        message="password updated successfully"
        return render(request,"facultychangepwd.html",{"fid":fid,"msg":message})
    else:
        message = "update unsuccessful"
        return render(request, "facultychangepwd.html", {"fid": fid, "msg": message})