from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return HttpResponse("<h1 align=center bgcolor=red>PFSD SDP PROJECT<h1>")
def demofunction1(request):
    return HttpResponse("<h1>KL UNIVERSITY")
def demofunction2(request):
    return HttpResponse("<font color='green'>student academic management system </font>")
def homefunction(request):
    return render(request,"index.html")
def aboutfunction(request):
    return render(request,'about.html')
def loginfunction(request):
    return render(request,'login.html')
def facultylogin(request):
    return render(request,"facultylogin.html")
def studentlogin(request):
    return render(request,"studentlogin.html")
def contactfunction(request):
    return render(request,'contact.html')




