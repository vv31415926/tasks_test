from django.urls import path
#from math_app  import  views
from .views import *
from math_app.views import Students_page#, Student_page

app_name = 'math_app'   # нужно обязательно - не будет адресации в шаблонах по имени  в include

urlpatterns = [
    path( '',                   main_page,            name='index'  ),
    path('table_tasks/',        TasksPage.as_view(),  name='tasks_table'),
    path('table_students/',     Students_page.as_view(),name='students_table'),
    path('login/',              login_page,           name='login'),
    #path('check/',              check_page,           name='check'),
    path('theme/',              ThemesPage.as_view(), name='themes'),
    path('partition/',          PartitionsPage.as_view(), name='partitions'),
    path('level/',              LevelsPage.as_view(), name='levels'),

    path('student/Lesson/<int:student_id>/',     StudentLessons.as_view(),      name='student_lessons'),

    path('task/<int:task_id>/',         ShowTask.as_view(),    name='task_one'),
    path('student/<int:student_id>/',   ShowStudent.as_view(), name='student_one'),
    path('version/<int:version_id>/',   ShowVersion.as_view(), name='version_one'),
    path('lesson/<int:lesson_id>/',     ShowLesson.as_view(),  name='lesson_one'),

]