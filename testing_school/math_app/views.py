from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import *
from .forms import *
from django.views.generic import *

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def main_page( request ):
    context = {'title': 'Проверка знаний по математике',
            }
    return render( request,
                   'math_app/index.html',
                   context=context )

class TasksPage( ListView ):
    model = Task
    template_name = 'math_app/table_tasks.html'
    # context_object_name = 'tasks' - не нужно т.к. определяется в context['tasks'] =  lst_data

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )

        tasks = Task.objects.all()
        lst_data = []
        for item in tasks:
            id = item.id
            vers = Version.objects.filter(task=id)
            lst = []
            for i, v in enumerate(vers):
                lst.append(v)
            dic = {'task': item, 'vers': lst, 'themenum': item.theme.num,
                   'themename': item.theme.name, 'partname': item.theme.partition.name,
                   'partnum': item.theme.partition.num,  'objvers':vers[0]  }
            lst_data.append(dic)

            context['title']= 'Задачи'
            context['nametable'] = 'Список задач'
            context['tasks'] =  lst_data

        return context



class StudentLessons( ListView ):
    model = Lesson
    template_name = 'math_app/lesson.html'
    context_object_name = 'student_lessons'
    pk_url_kwarg = 'student_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'уроки'
        context['obj'] = self.get_queryset()[0]
        context['namepage'] = 'студент: ' + self.get_queryset()[0].student.last_name+' '+self.get_queryset()[0].student.name
        return context

    def get_queryset(self):
        #print( '============',self.kwargs.keys() )
        return Lesson.objects.filter( student_id=self.kwargs['student_id'] )








class ShowTask( UpdateView ):
    form_class = TaskForm
    template_name = 'math_app/task.html'
    context_object_name = 'task_one'
    pk_url_kwarg = 'task_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )

        context['title'] = 'Задача'
        context['image'] = self.get_queryset()[0].img

        return context

    def get_queryset(self):
        return Task.objects.filter( pk=self.kwargs['task_id'] )

class Students_page( ListView ):
    model = Student
    template_name = 'math_app/table_students.html'
    context_object_name = 'students_table'   # path('table_students/', Students_page.as_view(),name='students_table'),

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['nametable'] = 'Список студентов'
        return context

class ShowStudent( UpdateView ):
    form_class = StudentForm
    template_name = 'math_app/student.html'
    context_object_name = 'student_one'
    pk_url_kwarg = 'student_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )

        context['title'] = 'Студент'
        context['obj'] = self.get_queryset()[0]

        return context

    def get_queryset(self):
        return Student.objects.filter( pk=self.kwargs['student_id'] )


class ShowVersion( UpdateView ):
    form_class = VersionForm
    template_name = 'math_app/version.html'
    context_object_name = 'version_one'
    pk_url_kwarg = 'version_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Весии ответов'
        #context['obj'] = self.get_queryset()[0]    дает context_object_name = 'version_one'
        return context

    def get_queryset(self):
        return Version.objects.filter( pk=self.kwargs['version_id'] )

class ShowLesson( UpdateView ):
    form_class = LessonForm
    template_name = 'math_app/lesson.html'
    context_object_name = 'lesson_one'
    pk_url_kwarg = 'lesson_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Урок'
        #context['obj'] = self.get_queryset()[0]    дает context_object_name = 'version_one'
        return context

    def get_queryset(self):
        return Version.objects.filter( pk=self.kwargs['version_id'] )



class ThemesPage( ListView ):
    model = Theme
    template_name = 'math_app/themes.html'
    context_object_name = 'themes'

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Темы'
        context['namepage'] = 'Темы задач'
        return context

class PartitionsPage( ListView ):
    model = Partition
    template_name = 'math_app/partitions.html'
    context_object_name = 'partitions'

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Разделы'
        context['namepage'] = 'Разделы'
        return context

class LevelsPage( ListView ):
    model = Level
    template_name = 'math_app/levels.html'
    context_object_name = 'levels'

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Уровни'
        context['namepage'] = 'Уровни сложности'
        return context


# def levels( request ):
#     level = Level.objects.all()
#     context = { 'title':'Уровень', 'level':level }
#     return render( request,
#                    'math_app/levels.html',
#                    context=context )


def login_page( request ):
    return render( request,
                   'math_app/login.html', )

