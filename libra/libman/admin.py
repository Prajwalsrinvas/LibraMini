from django.contrib import admin
from .models import Books, Student, Faculty, Issue, Return

# Register your models here.
admin.site.register(Books)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Issue)
admin.site.register(Return)
