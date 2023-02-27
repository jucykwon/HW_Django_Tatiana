from django.http import HttpResponse
from django.shortcuts import render

from .models import Student


# Create your views here.
# HTTPRequest
# HttpResponse

def index(request):
    students = Student.objects.all().order_by('birthday')
    # string = '<br>'.join(str(student) for student in students)
    string = '<table><thead><tr><th>First Name</th><th>Last Name</th><th>Email</th><th>Birthday</th><thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.birthday}</td></tr>'
    string += '</tbody></table>'
    return HttpResponse(string)
