from django.urls import path
from . import views
urlpatterns = [
    path('',views.to_base,name='go_to_base'),
    path('home/',views.base,name='base'),
    path('home/signin/',views.signin,name='signin'),
    path('home/signout',views.signout,name='signout'),
    path('home/teachers',views.teach_Dash,name='Teachers'),
    path('home/teachers/attendance',views.teach_attendance,name="Teach_attendance"),
    path('home/teachers/attendance/morning_absent/<int:id>', views.morning_absent, name="Absent assign"),
    path('home/teachers/attendance/afternoon_absent/<int:id>', views.afternoon_absent, name="Absent assign(1)"),
    path('home/teachers/attendance/morning_present/<int:id>', views.morning_present, name="Present assign"),
    path('home/teachers/attendance/afternoon_present/<int:id>', views.afternoon_present, name="Present assign(1)"),  
    path('home/teachers/marks', views.marks_page, name='Marks'),
    path('home/teachers/marks/<int:id>',views.marks_edit,name='Marks_assign'),
    path('home/teachers/adddExam',views.create_exam,name='Addexam'),
    path('dummy/',views.dummy,name='dummy'),
]