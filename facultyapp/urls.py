from django.urls import path
from . import views

urlpatterns = [
    path("facultyhome",views.facultyhome,name="facultyhome"),
    path("checkfacultylogin",views.checkfacultylogin,name="checkfacultylogin"),
    path("myfcourses",views.facultycourses,name="facultycourses"),
    path("facultyaddcontent",views.facultyaddcontent,name="facultyaddcontent"),
    path("facultychangepwd",views.facultychangepwd,name="facultychangepwd"),
    path("facultyupdatepwd",views.facultyupdatepwd,name="facultyupdatepwd"),
]