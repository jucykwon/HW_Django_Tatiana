from django.db.models import Q
# from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from .forms import UpdateStudentForm, CreateStudentForm
from .models import Student
# from .utils import format_list_students

from webargs.fields import Str
from webargs.djangoparser import use_args


# Create your views here.
# HTTPRequest
# HttpResponse

def view_with_param(request, value):
    return HttpResponse(f'With param: "{value}"')


def view_without_param(request):
    return HttpResponse('Without param')


def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)
def get_students(request, args):
    students = Student.objects.all().order_by('birthday')
    #    if 'first_name' in args:
    #        students = students.filter(first_name=args['first_name'])
    #    if 'last_name' in args:
    #        students = students.filter(last_name=args['last_name'])
    if len(args) and (args.get('first_name') or args.get('last_name')):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )
    #  form =  '''
    #     <body>
    # <form method="get">
    #     <label for="first_name">First name:</label><br>
    #     <input type="text" id="first_name" name="first_name"><br><br>
    #     <label for="last_name">Last name:</label><br>
    #     <input type="text" id="last_name" name="last_name"><br><br>
    #     <input type="submit" value="Submit">
    # </form>
    # '''
    # string = form + format_list_students(students)
    # response = HttpResponse(string)
    # return response
    return render(
        request=request,
        template_name='students/list.html',
        context={'title': 'List of students', 'students': students}
    )


def detail_student(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/detail.html', {'title': 'Detail of student', 'student': student})


# @csrf_exempt
def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
        <input type="submit" value="Submit"><br><br>
        <a href="/students/"> Back to list</a>
        </form> 
        '''

    return HttpResponse(html_form)


def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
        <input type="submit" value="Submit"><br><br>
        <a href="/students/">Back to List</a>
        </form> 
        '''

    return HttpResponse(html_form)
