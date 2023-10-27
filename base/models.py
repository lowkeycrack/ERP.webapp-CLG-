from django.db import models
from django.contrib.auth.models import User
# Create your models here.


@property
def is_admin(self):
    return getattr(self, 'admin', None)

@property
def is_faculty(self):
    return getattr(self, 'staff', None)

@property
def is_student(self):
    return getattr(self, 'student', None)

User.add_to_class('is_student', is_student)
User.add_to_class('is_admin', is_admin)
User.add_to_class('is_faculty', is_faculty)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    qualifications = models.ManyToManyField('Qualification', blank=True)

    def __str__(self):
        return self.user.get_full_name()
    
class Qualification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_earned = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Owner can be either a student or staff.

    def __str__(self):
        return self.name

class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    courses = models.ManyToManyField('Course', blank=True)
    qualifications = models.ManyToManyField(Qualification, blank=True)
    batch=models.ForeignKey('classes', on_delete=models.CASCADE, null= True)


class course(models.Model):
    name=models.CharField(max_length=50)
    HOD=models.ForeignKey('staff', on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class branch(models.Model):
    name=models.CharField(max_length=50)
    course=models.ForeignKey('course', on_delete=models.CASCADE)
    head=models.ForeignKey('staff', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class classes(models.Model):
    year=models.IntegerField(null=True)
    section=models.CharField(max_length=1)
    course=models.ForeignKey('course', on_delete=models.CASCADE)
    branch=models.ForeignKey(branch, on_delete=models.CASCADE)
    proctor=models.ForeignKey('staff', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.course} {self.branch} year:{self.year} section:{self.section}"

class subject(models.Model):
    batch=models.ForeignKey('classes', on_delete=models.CASCADE)
    faculty=models.ForeignKey('staff', on_delete=models.CASCADE)
    subject_name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    



class timetable(models.Model):
    batch=models.ForeignKey('classes', on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.batch.section
    

class tablerow(models.Model):
   start_time=models.TimeField()
   end_time=models.TimeField()
   batch=models.ForeignKey('classes', on_delete=models.CASCADE)
   lecturer=models.ForeignKey('staff', on_delete=models.CASCADE)
   subject=models.ForeignKey(subject, on_delete=models.CASCADE)

class topic(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(topic, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=50)
    participants=models.ManyToManyField(User, related_name="participants")
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    class Meta:
        ordering= ['-updated', '-created']
    
    def __str__(self):
        return str(self.name)
class message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now=True)
    def __str__(self):
        return self.body[0:50]



class event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    event_image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    max_participants = models.PositiveIntegerField(null=True, blank=True)
    event_type = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    additional_information = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title