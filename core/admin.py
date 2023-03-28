from django.contrib import admin

from .models import User,Degree
from .models import Course,Document,Semester,Speciality,DocumentType,PlanningExam
admin.site.register(User)

admin.site.register(Speciality)


admin.site.register(Course)

admin.site.register(Document)
admin.site.register(DocumentType)


admin.site.register(Degree)

admin.site.register(Semester)

admin.site.register(PlanningExam)
