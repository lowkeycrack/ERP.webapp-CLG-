from django.contrib import admin
from . models import course,Room, topic , message, classes, subject, staff, branch, timetable, tablerow, student, Admin, event

# Register your models here.
admin.site.register(course)
admin.site.register(classes)
admin.site.register(subject)
admin.site.register(staff)
admin.site.register(branch)
admin.site.register(timetable)
admin.site.register(tablerow)
admin.site.register(student)
admin.site.register(Admin)
admin.site.register(Room)
admin.site.register(topic)
admin.site.register(message)
admin.site.register(event)


