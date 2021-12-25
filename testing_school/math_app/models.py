from django.db import models

# Create your models here.
from django.urls import reverse

class Task( models.Model ):
    numtask = models.IntegerField( default=0 , verbose_name='Номер')
    variant = models.IntegerField( default=0, verbose_name= 'Вариант')
    question = models.TextField(blank=True, verbose_name='Условие')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    img = models.ImageField( upload_to='task', blank=True, null=True, verbose_name= 'Чертеж')
    numclass = models.IntegerField(default=0, verbose_name='класс')

    theme = models.ForeignKey( 'Theme', on_delete=models.SET_NULL, null=True, blank=True, verbose_name= 'Тема')
    level = models.ForeignKey( 'Level', on_delete=models.SET_NULL, null=True, blank=True, verbose_name= 'Уровень')

    def __str__(self):
        return f'{self.numtask}: {self.question}'

    def get_absolute_url(self):
        return reverse( 'math_app:task_one',  kwargs={'task_id':self.pk} )

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'

class Student( models.Model ):
    name = models.CharField( max_length=50, verbose_name= 'Имя' )
    last_name = models.CharField(max_length=50, verbose_name= 'Фамилия' )
    email = models.EmailField( max_length=254, verbose_name= 'Почта' )
    num_class = models.IntegerField( verbose_name= 'Класс' )
    letter_class = models.CharField( max_length=1, verbose_name= 'литера класса'  )
    date_reg = models.DateTimeField( auto_now_add=True, verbose_name= 'регистрация' )
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.last_name} {self.name}, {self.num_class}{self.letter_class}, {self.email}'

    def get_absolute_url(self):
        return reverse( 'math_app:student_one',  kwargs={'student_id':self.pk} )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'name']

class Partition( models.Model ):
    num = models.IntegerField()
    name = models.CharField( max_length=32 )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

class Version(models.Model):
    npp = models.IntegerField(default=0, verbose_name= 'N п/п' )
    answer = models.CharField(max_length=100, verbose_name= 'Ответ' )
    correct = models.BooleanField(default=False, verbose_name= 'Правильно' )
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, verbose_name= 'Задача' )

    def __str__(self):
        return f'{self.answer}'

    def get_absolute_url(self):
        return reverse( 'math_app:version_one',  kwargs={'version_id':self.pk} )

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

class Lesson( models.Model ):
    answer = models.IntegerField(default=0)
    correctly = models.CharField( max_length=13, default='не проверено')
    begin_lesson = models.DateTimeField(auto_now_add=True)
    date_answer = models.DateTimeField(  null=True, blank=True  )
    date_check = models.DateTimeField(  null = True, blank = True  )

    task = models.ForeignKey(  'Task', on_delete=models.CASCADE , null=True)     #? , null=True
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True )
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        s = str(self.task)[0:50]
        return f'{self.student}: ответ {self.answer}, оценка "{self.correctly}", задание "{s}..."'

    def get_absolute_url(self):
        return reverse( 'math_app:lesson_one',  kwargs={'lesson_id':self.pk} )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Level( models.Model ):
    num = models.IntegerField()
    name = models.CharField( max_length=16 )

    def __str__(self):
        return f'{self.num}-{self.name}'

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'
        ordering = ['num']

class Theme( models.Model ):
    num = models.IntegerField()
    name = models.CharField( max_length=512 )
    partition = models.ForeignKey( 'Partition', on_delete=models.SET_NULL , null=True )

    def __str__(self):
        return f'{self.num}-{self.name}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['name']