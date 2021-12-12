from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Student, Lesson, Version
from .forms import Lesson_form

# Create your views here.
def main_page( request ):
    return render( request,
                   'math_app/index.html' )

def table_page( request ):
    tasks = Task.objects.all()
    dic_task= {}
    dic_v = {}
    lst_data = []

    for item in tasks:
        id = item.id
        vers = Version.objects.filter( task = id )
        lst= []
        for i,v in enumerate(vers):
           lst.append(v)
        dic = { 'task':item, 'vers':lst }
        lst_data.append( dic )
    return render( request,
                   'math_app/tables.html',
                   context={ 'nametable':'Список задач', 'tasks':lst_data } )

def tasks_page( request ):
    tasks = Task.objects.all()
    lst_data = []

    for item in tasks:
        id = item.id
        vers = Version.objects.filter( task = id )
        lst= []
        for i,v in enumerate(vers):
           lst.append(v)
        dic = { 'task':item, 'vers':lst }
        lst_data.append( dic )
    return render( request,
                   'math_app/table_tasks.html',
                   context={ 'nametable':'Список задач', 'tasks':lst_data } )

def students_page( request ):
    students = Student.objects.all()

    return render( request,
                   'math_app/table_students.html',
                   context={ 'nametable':'Список студентов', 'students':students } )

def login_page( request ):
    return render( request,
                   'math_app/login.html', )

def lesson_page( request ):
    task_data = Task.objects.first()
    if request.method == 'post':
        les_form = Lesson_form( request.POST )
        #if les_form.is_valid()
    else:
        les_form = Lesson_form(  )
    return render( request,
                   'math_app/lesson.html', {'form':les_form, 'task_data':task_data } )