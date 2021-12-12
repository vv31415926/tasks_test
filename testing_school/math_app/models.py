from django.db import models

# Create your models here.

class Task(models.Model):
    numtask = models.IntegerField(default=0)
    variant = models.IntegerField(default=0)
    group = models.CharField(max_length=5)
    question = models.TextField(blank=True)
    img = models.ImageField( upload_to='task', blank=True, null=True )


    def __str__(self):
        return f'{self.group}.{self.variant}.{self.numtask}: {self.question}'


class Version(models.Model):
    npp = models.IntegerField(default=0)
    variant = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.npp}) {self.variant} - {self.correct}'

class Student( models.Model ):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    num_class = models.IntegerField()
    letter_class = models.CharField( max_length=1 )

    def __str__(self):
        return f'{self.name}, {self.num_class}{self.letter_class}, {self.email}'


class Lesson( models.Model ):
    answer = models.IntegerField(default=0)
    correctly = models.CharField( max_length=13, default='не проверено')
    begin = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(  Task, on_delete=models.CASCADE , null=True)     #? , null=True
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True )

    def __str__(self):
        s = str(self.task)[0:50]
        return f'{self.student}: ответ {self.answer}, оценка "{self.correctly}", задание "{s}..."'

