from django.urls import path
from math_app  import  views


app_name = 'math_app'   # нужно обязательно - не будет адресации в шаблонах по имени  в include

urlpatterns = [
    path( '', views.main_page, name='index'  ),
    #      адрес     функ-вьюшка     обращение из html
    #path('table/', views.table_page, name='table'),  # с какого адреса запускать вьюшку
    path('table_tasks/', views.tasks_page, name='tasks_table'),
    path('table_students/', views.students_page, name='students_table'),
    path('login/', views.login_page, name='login'),
    path('lesson/', views.lesson_page, name='lesson'),
    #path('students/', views.students_page, name='students'),  # с какого адреса запускать вьюшку
    #path('tasks/', views.tasks_page, name='tasks'),
    #path('lessons/', views.lessons_page, name='lessons'),
]