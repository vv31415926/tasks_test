from django.core.management.base import BaseCommand
from math_app.models import Student, Task, Version, Lesson

class Command( BaseCommand ):
    def handle(self, *args, **options):
        stud = Student.objects.filter( num_class=10 )
        stud.delete()

        tsk = Task.objects.filter( group='AA5')  # AA5 engl
        tsk.delete()

