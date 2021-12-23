from django.core.management.base import BaseCommand
from math_app.models import Student, Task, Version, Lesson

class Command( BaseCommand ):
    def handle(self, *args, **options):
        stud = Student.objects.all()
        stud.delete()

        tsk = Task.objects.all()  # A5 engl
        tsk.delete()

