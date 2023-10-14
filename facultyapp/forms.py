from django import forms

from .models import CourseContent


class AddContentForm(forms.ModelForm):
    class Meta:
        model=CourseContent
        fields="__all__"

