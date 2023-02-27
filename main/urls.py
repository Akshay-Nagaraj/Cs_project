from django.urls import path
from . import views
urlpatterns = [
    path('',views.to_base,name='go_to_base'),
    path('home/',views.base,name='base'),
    path('home/signin/',views.signin,name='signin'),
    path('home/signout',views.signout,name='signout'),
    path('home/teachers',views.teach_Dash,name='Teachers'),
    path('home/teachers/attendance',views.teach_attendance,name="Teach_attendance"),
    path('dummy/',views.dummy,name='dummy'),
]