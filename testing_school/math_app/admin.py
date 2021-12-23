from django.contrib import admin
from .models import *

# class StudentAdmin(  admin.ModelAdmin ):
#     list_display = ('last_name', 'name' )
#     prepopulated_fields = {'slug':('last_name',)}
# class TaskAdmin(  admin.ModelAdmin ):
#     prepopulated_fields = {'slug':('group', 'numtask', 'variant',)}
# class VersionAdmin(  admin.ModelAdmin ):
#     prepopulated_fields = {'slug':('id',)}
# class LessonAdmin(  admin.ModelAdmin ):
#     prepopulated_fields = {'slug':('id',)}
# class ThemeAdmin(  admin.ModelAdmin ):
#     prepopulated_fields = {'slug':('name', )}
# class SubjectAdmin(  admin.ModelAdmin ):
#     prepopulated_fields = {'slug':('name', )}

# admin.site.register( Student, StudentAdmin )
# admin.site.register( Task, TaskAdmin )
# admin.site.register( Version, VersionAdmin )
# admin.site.register( Lesson, LessonAdmin  )
# admin.site.register( Theme, ThemeAdmin )
# admin.site.register( Subject, SubjectAdmin )

admin.site.register( Student )
admin.site.register( Task )
admin.site.register( Version )
admin.site.register( Lesson )
admin.site.register( Theme )
admin.site.register( Partition )
admin.site.register( Level )

