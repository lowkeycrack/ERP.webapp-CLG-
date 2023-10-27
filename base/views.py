from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from . forms import *
from . models import *
from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
import logging
from .helpers import *


# Create your views here.


@login_required(login_url='login')
@admin_required(login_url='login')
def home(request):
    user=request.user
    if user.is_admin:
        return render(request, 'base/admin/admin_dashboard.html')
    else:
        return redirect("login")


def login_page(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_student:
                return redirect("student_dashboard")
            elif user.is_faculty:
                return redirect("staff_dashboard")
            else:
                return HttpResponse("no role specified")
        else:
            return HttpResponse('form is invalid')
            
    form=AuthenticationForm()
    context={'form':form}
    return render(request, 'base/admin/login.html',context)



@login_required(login_url='login')
@admin_required(login_url='login')
def update_profile(request):
    return render(request, "base/admin/update_profile.html")



@login_required(login_url='login')
@admin_required(login_url='login')
def add_course(request):
    if request.method=='POST':
        form=createcourseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_course')
        else:
            print(form.errors)
            HttpResponse('somethimg is wrong with the request')
    form = createcourseform()
    context={"form":form} 
    return render(request,"base/admin/add_course.html",context)




@login_required(login_url='login')
@admin_required(login_url='login')
def manage_course(request):
    courses=course.objects.all()
    context={"courses":courses}
    return render(request, "base/admin/manage_course.html", context)




@login_required(login_url='login')
@admin_required(login_url='login')
def add_student(request):
     if request.method == "POST":
        student_form = studentcreationform(request.POST)
        if student_form.is_valid():
            new_user = student_form.save()      
            return redirect("manage_student")
        else:
            print(student_form.errors)
            return HttpResponse("something went wrong")
     student_form = studentcreationform()
     context = {"form": student_form}
     return render(request, "base/admin/add_student.html", context)



@login_required(login_url='login')
@admin_required(login_url='login')
def manage_student(request):
    students=User.objects.filter(student__isnull=False)
    context={"students":students}
    return render(request,'base/admin/manage_student.html', context)




@login_required(login_url='login')
@admin_required(login_url='login')
def add_staff(request):
    if request.method == "POST":
        staff_form = StaffCreationForm(request.POST)
        if staff_form.is_valid():
            new_user = staff_form.save()      
            return redirect("manage_staff")
        else:
            print(staff_form.errors)
            return HttpResponse("something went wrong")
    staff_form = StaffCreationForm()
    context = {"form": staff_form}
    return render(request, "base/admin/add_staff.html", context)




@login_required(login_url='login')
@admin_required(login_url='login')
def manage_staff(request):
    faculties=User.objects.filter(staff__isnull=False)
    context={"faculties":faculties}
    return render(request, "base/admin/manage_staff.html",context)




@login_required(login_url='login')
@admin_required(login_url='login')
def add_subject(request):
    if request.method=='POST':
        form=createsubjectform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_subject")
        else:
            return HttpResponse('something went wrong')
    form=createsubjectform()
    context={"form":form}
    return render(request,'base/admin/add_subject.html', context)

@login_required(login_url='login')
@admin_required(login_url='login')
def edit_subject(request, pk):
    edit_subject=subject.objects.get(id=pk)
    if request.method=='POST':
        form=createsubjectform(request.POST, instance=edit_subject)
        if form.is_valid():
            form.save()
            return redirect('manage_subject')
        else:
            HttpResponse('somethimg is wrong with the request')
    form=createsubjectform(instance=edit_subject)
    context={"class":edit_subject,"form":form}
    return render(request, 'base/admin/edit_subject.html', context)

    
@login_required(login_url='login')
@admin_required(login_url='login')
def delete_subject(request, pk):
    delete_subject=subject.objects.get(id=pk)
    delete_subject.delete()
    return redirect("manage_subject")



@login_required(login_url='login')
@admin_required(login_url='login')
def manage_subject(request):
    subjects=subject.objects.all()
    context={"subjects":subjects}
    return render(request, "base/admin/manage_subject.html", context)




@login_required(login_url='login')
@admin_required(login_url='login')
def create_class(request):
    if request.method=='POST':
        form=createclassform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_class')
        else:
            HttpResponse('somethimg is wrong with the request')
    form = createclassform()
    context={"form":form} 
    return render(request,"base/admin/create_classes.html",context)

@login_required(login_url='login')
@admin_required(login_url='login')
def edit_class(request, pk):
    edit_class=classes.objects.get(id=pk)
    if request.method=='POST':
        form=createclassform(request.POST, instance=edit_class)
        if form.is_valid():
            form.save()
            return redirect('manage_class')
        else:
            HttpResponse('somethimg is wrong with the request')
    form=createclassform(instance=edit_class)
    context={"class":edit_class,"form":form}
    return render(request, 'base/admin/edit_class.html', context)


@login_required(login_url='login')
@admin_required(login_url='login')
def delete_class(request, pk):
    delete_class=classes.objects.get(id=pk)
    delete_class.delete()
    return redirect("manage_class")


@login_required(login_url='login')
@admin_required(login_url='login')
def manage_class(request):
    batches=classes.objects.all()
    context={"classes":batches}
    return render(request, "base/admin/manage_classes.html", context)




@login_required(login_url='login')
@admin_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect("login")



@login_required(login_url='login')
@admin_required(login_url='login')
def edit_course(request, pk):
    edit_course=course.objects.get(id=pk)
    if request.method=='POST':
        form=createcourseform(request.POST, instance=edit_course)
        if form.is_valid():
            form.save()
            return redirect('manage_course')
        else:
            HttpResponse('somethimg is wrong with the request')
    form=createcourseform(instance=edit_course)
    context={"course":edit_course,"form":form}
    return render(request, 'base/admin/edit_course.html', context)


@login_required(login_url='login')
@admin_required(login_url='login')
def delete_course(request, pk):
    delete_course=course.objects.get(id=pk)
    delete_course.delete()
    return redirect("manage_course")

logger = logging.getLogger(__name__)

@login_required(login_url='login')
@admin_required(login_url='login')
def edit_student(request, pk):
    edit_student=student.objects.get(user__id=pk)
    if request.method=='POST':
        form=StudentEditForm(request.POST, instance=edit_student)
        if form.is_valid():
            form.save()
            return redirect("manage_student")
        else:
            print(form.errors)
            return redirect('admin_dashboard')
            logger.error(form.errors)
            print(form.errors)
    form=StudentEditForm(instance=edit_student, initial={
        'first_name': edit_student.user.first_name,
        'last_name':edit_student.user.last_name,
        'username': edit_student.user.username,
        'email':edit_student.user.email,
    })
    context={"student":edit_student,"form":form}
    return render(request, 'base/admin/edit_student.html', context)

@login_required(login_url='login')
@admin_required(login_url='login')
def delete_student(request, pk):
    delete_student=student.objects.get(user__id=pk)
    delete_student.delete()
    return redirect("manage_student")



@login_required(login_url='login')
@admin_required(login_url='login')
def edit_staff(request, pk):
    edit_staff=staff.objects.get(user__id=pk)
    if request.method=='POST':
        form=staffeditform(request.POST, instance=edit_staff)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
        else:
            HttpResponse('somethimg is wrong with the request')
    form=staffeditform(instance=edit_staff, initial={
            'first_name': edit_staff.user.first_name,
            'last_name':edit_staff.user.last_name,
            'username': edit_staff.user.username,
            'email':edit_staff.user.email,
        })
    context={"staff":edit_staff,"form":form}
    return render(request, 'base/admin/edit_staff.html', context)


@login_required(login_url='login')
@admin_required(login_url='login')
def delete_staff(request, pk):
    delete_staff=staff.objects.get(user__id=pk)
    delete_staff.delete()
    delete_staff.delete
    return redirect("manage_staff")

@staff_required(login_url='login')
@login_required(login_url='login')
def staff_dashboard(request):
    return render(request,'base/staff/home.html')


def student_dashboard(request):
    return render(request,'base/student/home.html')

@login_required(login_url='login')
def room_home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    topics=topic.objects.all()
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q))
    room_count=rooms.count()
    chats=message.objects.all().order_by('-updated')
    context = {"rooms":rooms,"topics":topics,"room_count":room_count,"chats":chats}
    return render(request, 'base/room/home.html',context)


@login_required(login_url='login')
def room(request , pk):
    room=Room.objects.get(id=pk)
    participants=room.participants.all()
    roomessage=room.message_set.all().order_by('created')
    if request.method == 'POST':
        chat=message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {'room':room,'chats':roomessage, 'users':participants}
    return render(request, 'base/room/room.html',context)




@login_required(login_url='login')
@staff_required(login_url='login')
def create_room(request):
    form=roomform()
    if request.method == 'POST':
        form = roomform(request.POST)
        if form.is_valid():
            created_room=form.save(commit=False)
            created_room.host=request.user
            created_room.save()
            return redirect('room_home')
    context={'form':form}
    return render(request, 'base/room/room_form.html', context)



@login_required(login_url='login')
@staff_required(login_url='login')
def update_room(request,pk):
    room=Room.objects.get(id=pk)
    # if request.user != room.host:
    #     return HttpResponse('you are not allowed for the operation')
    form=roomform(instance=room)
    if request.method=='POST':
        form=roomform(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_home')
    context={'form':form}
    return render(request, 'base/room/room_form.html', context)


def manage_events(request):
    events = event.objects.all()
    context = {'events': events}
    return render(request,'base/admin/manage_events.html', context)



def add_events(request):
    staff_users =User.objects.filter(staff__isnull=False) 
    if request.method == 'POST':
        form = eventform(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Set the organizer to the currently logged-in user
            event.save()
            return redirect('manage_events')
        else:
            print(form.errors)
              # Redirect to the list of events or any other view you prefer
    else:
        form = eventform()
    
    context = {'form': form, 'staff_users':staff_users}
    return render(request, 'base/admin/add_events.html', context)

@login_required(login_url='login')
def edit_events(request, pk):
    edit_event=event.objects.get(id=pk)
    if request.method=='POST':
        form=eventform(request.POST, instance=edit_event)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
        else:
            HttpResponse('somethimg is wrong with the request')
    form=eventform(instance=edit_event)
    staff_user=User.objects.filter(staff__isnull=False)
    context={"event":edit_event,"form":form,"staff_user":staff_user}
    return render(request, 'base/admin/edit_event.html', context)


@login_required(login_url='login')
@admin_required(login_url='login')
def delete_event(request, pk):
    delete_events=event.objects.get(id=pk)
    delete_events.delete()
    return redirect("manage_events")
    

def events(request):
    events = event.objects.filter(is_active=True)  # Fetch all active events from the database
    return render(request, 'base/student/events.html', {'events': events})

