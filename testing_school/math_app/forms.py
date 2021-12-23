from django import forms
from .models import *

class Check_form( forms.ModelForm ):
    pass

class TaskForm( forms.ModelForm ):
    #numtask = forms.IntegerField()
    #question = forms.CharField( widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    class Meta:
        model=Task
        fields=['numtask', 'variant', 'question', 'comment', 'numclass','level','theme','img']
        widgets = {  'question': forms.Textarea(attrs={'cols': 35, 'rows':5})    }

class StudentForm( forms.ModelForm ):
    class Meta:
        model=Student
        fields=['last_name', 'name', 'email', 'num_class', 'letter_class']

class VersionForm( forms.ModelForm ):
    class Meta:
        model=Version
        fields=['npp', 'answer', 'correct' ]

class LessonForm( forms.ModelForm ):
    class Meta:
        model=Lesson
        fields=['answer', 'correctly' ]