from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="admin_dashboard"),
    path('student/',views.student_dashboard, name="student_dashboard"),
    path('staff/',views.staff_dashboard, name="staff_dashboard"),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('add_course/',views.add_course,name="add_course"),
    path('manage_course/',views.manage_course,name="manage_course"),
    path('add_student/',views.add_student,name="add_student"),
    path('manage_student/',views.manage_student,name="manage_student"),
    path('add_staff/',views.add_staff,name="add_staff"),
    path('manage_staff/',views.manage_staff,name="manage_staff"),
    path('login/',views.login_page, name="login"),
    path('add_subject/', views.add_subject, name="add_subject"),
    path('manage_subject/', views.manage_subject, name="manage_subject"),
    path('manage_events/', views.manage_events, name="manage_events"),
    path('add_events/', views.add_events, name="add_events"),
    path('edit_events/<str:pk>', views.edit_events, name="edit_events"),
    path('delete_events/<str:pk>', views.delete_event, name="delete_event"),
    path('edit_class/<str:pk>', views.edit_class, name="edit_class"),
    path('delete_class/<str:pk>', views.delete_class, name="delete_class"),
    path('edit_subject/<str:pk>', views.edit_subject, name="edit_subject"),
    path('delete_subject/<str:pk>', views.delete_subject, name="delete_subject"),
    path('create_class/', views.create_class, name="create_class"),
    path('logout/',views.logout_page, name="logout"),
    path('manage_class/', views.manage_class, name="manage_class"),
    path("edit_staff/<str:pk>",views.edit_staff,name="edit_staff"),
    path("delete_staff/<str:pk>",views.delete_staff,name="delete_staff"),
    path("edit_student/<str:pk>",views.edit_student,name="edit_student"),
    path("delete_student/<str:pk>",views.delete_student,name="delete_student"),
    path("edit_course/<str:pk>",views.edit_course,name="edit_course"),
    path("delete_course/<str:pk>",views.delete_course,name="delete_course"),
    path("room_home/",views.room_home,name="room_home"),
    path("room/<str:pk>",views.room,name="room"),
    path("create_room/",views.create_room,name="create_room"),
    path("update_room/<str:pk>",views.update_room,name="update_room"),
    path("events/",views.events,name="events"),


]


