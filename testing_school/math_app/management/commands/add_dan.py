# Импортируемые данные
lst_student = [
{'name':'Воробъев','email':'a1@mail.ru','class':'10','ch':'А'},
{'name':'Щеглов','email':'a2@mail.ru','class':'10','ch':'Б'},
{'name':'Синицин','email':'a3@mail.ru','class':'10','ch':'В'},
{'name':'Соколов','email':'a4@mail.ru','class':'10','ch':'Г'},
{'name':'Орлов','email':'a5@mail.ru','class':'10','ch':'А'},
{'name':'Цаплин','email':'a6@mail.ru','class':'10','ch':'Б'},
{'name':'Снигирев','email':'a7@mail.ru','class':'10','ch':'В'},
{'name':'Кукушкин','email':'a8@mail.ru','class':'10','ch':'Г'},
{'name':'Савушкин','email':'a9@mail.ru','class':'10','ch':'А'},
{'name':'Куропаткин','email':'a0@mail.ru','class':'10','ch':'Б'}
]
# AA5 engl
lst_task=[
{'question':'Точка движктся по закону S(t)=t^3-2*t^2. ' \
            'Выберите какой из формул задается скорость движения этой точки в момент времени t.',
            'numtask':'3','variant':'3','group':'AA5',
            'version': [{'variant':'3*t^2-2','correct':'0','npp':'1'},
                        {'variant':'t^2-4*t','correct':'0','npp':'2'},
                        {'variant':'t^4/4-2*t^3/3','correct':'0','npp':'3'},
                        {'variant':'3*t^2-4*T','correct':'1','npp':'4'} ]},
{'question':'Зависимость температуры T тела от времени задана уравнением' \
            'T=1/2*T^2-2*t+5. С какой скоростью нагревается это тело в момент времени t=5с ?',
            'numtask':'4','variant':'3','group':'AA5',
            'version': [{'variant':'3','correct':'1','npp':'1'},
                        {'variant':'-8','correct':'0','npp':'2'},
                        {'variant':'7,5','correct':'0','npp':'3'},
                        {'variant':'7','correct':'0','npp':'4'} ]},
{'question':'При движении тела по прямой расстояние S(t) в метрахот начальной точки M ' \
            'изменяется по закону S(t)=3*t^3+2*t^2+4*t+5 (t-время в секундах). Через сколько секунд ' \
            'после начала движения мгновенное  ускорение тела будет равно 58 м/с^2 ?',
            'numtask':'5','variant':'3','group':'AA5',
            'version': [{'variant':'5c','correct':'0','npp':'1'},
                        {'variant':'3c','correct':'1','npp':'2'},
                        {'variant':'2c','correct':'0','npp':'3'},
                        {'variant':'0','correct':'0','npp':'4'} ]}
]
# Импорт:
from django.core.management.base import BaseCommand
from math_app.models import Student, Task, Version, Lesson

class Command( BaseCommand ):
    def handle(self, *args, **options):
        stud = Student.objects.filter( num_class=10 )
        if len( stud ) == 0:
            for s in lst_student:
                Student.objects.create(  name=s['name'], email=s['email'], num_class=int(s['class']), letter_class=s['ch'])
        tsk = Task.objects.filter( group='AA5')
        if len(tsk) == 0:
            for t in lst_task:
                Task.objects.create( question=t['question'], numtask=t['numtask'], variant=t['variant'], group=t['group'] )
                t_id = Task.objects.get(numtask=t['numtask']).id
                #print( t_id, type(t_id))
                for v in t['version']:
                    Version.objects.create( npp=v['npp'], variant=v['variant'], correct=v['correct'], task_id=t_id )
        # уроки
        import random
        stud = Student.objects.all()
        tsk = Task.objects.all()

        for s in stud:
            s_id = s.id
            for t in tsk:
                t_id = t.id
                Lesson.objects.create( answer=random.randint(1,4), student_id=s_id, task_id=t_id  )
