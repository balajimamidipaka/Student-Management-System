from django import forms
from .models import Faculty, Student


class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"password"}
        labels={"facultyid":"Enter Faculty Id","gender":"Select Gender","fullname":"Enter Full Name"}

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"password"}
        labels={"studentid":"Enter Student Id"}
class UpdateFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"facultyid","gender","password"}



