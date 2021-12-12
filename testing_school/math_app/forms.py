from django import forms
from .models import *

class Lesson_form( forms.Form ):

    task_data = Task.objects.first()
    task = forms.CharField( widget=forms.Textarea(attrs={'cols': 60, 'rows':4}),
                            label='Задача',
                            initial=task_data.question )
    version = forms.ModelChoiceField( widget=forms.RadioSelect,
                                      queryset=Version.objects.filter( task=task_data.id),
                                      label='Вариант ответа'  )

# ---------------------------------------------------------------------------------------------------------------
#class  Login_form( forms.Form ):
#    login = forms.EmailInput( max_length=25 )

