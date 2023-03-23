from django.contrib import admin
from django.urls import path

from groups.views import get_groups, create_group_view, update_group, detail_group
from students.views import index, get_students, create_student_view, update_student, detail_student
from teachers.views import get_teachers, create_teacher_view, update_teacher, detail_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student_view),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher_view),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/detail/<int:pk>/', detail_teacher),
    path('groups/', get_groups),
    path('groups/create/', create_group_view),
    path('groups/update/<int:pk>/', update_group),
    path('groups/detail/<int:pk>/', detail_group),
]

