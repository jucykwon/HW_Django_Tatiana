from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]


