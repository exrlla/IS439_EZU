from django.contrib import admin
from django.urls import path
from courseinfo.views import (
    instructor_list_view,
    section_list_view,
    course_list_view,
    semester_list_view,
    student_list_view,
    registration_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructor/', instructor_list_view),
    path('section/', section_list_view),
    path('course/', course_list_view),
    path('semester/', semester_list_view),
    path('student/', student_list_view),
    path('registration/', registration_list_view),
]

