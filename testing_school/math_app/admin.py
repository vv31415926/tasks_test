from django.contrib import admin
from .models import Student, Task, Version, Lesson

# Register your models here.
admin.site.register( Student )
admin.site.register( Task )
admin.site.register( Version )
admin.site.register( Lesson )