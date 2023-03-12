from django.contrib import admin
from django.urls import path


from students.views import index, get_students, create_student_view
from students.views import view_without_param
from students.views import view_with_param

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #    path('test/route/param/', view_without_param),
    #    path('test/route/<str:value>/', view_with_param),
    path('students/', get_students),
    path('students/create/', create_student_view),
]
