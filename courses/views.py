from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import UpdateCourseForm, CreateCourseForm, FilterCourseForm
from .models import Course

from webargs.fields import Str
from webargs.djangoparser import use_args


def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'course_name': Str(required=False),
        'start_date': Str(required=False),
        'end_date': Str(required=False),
    },
    location='query',
)
def get_courses(request, args):
    courses = Course.objects.all().order_by('course_name')
    filter_form = FilterCourseForm(data=request.GET, queryset=courses)
    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'filter_form': filter_form,
        }
    )


def detail_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'title': 'Detail of course', 'course': course})


def create_course_view(request):
    if request.method == 'GET':
        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/create.html', {'form': form})


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = UpdateCourseForm(instance=course)
    elif request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/update.html', {'form': form})

    return HttpResponse(html_form)


def delete_course(request, pk):
    st = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('courses:list'))
    if request.method == 'GET':
        return render(request, 'courses/delete.html', {'course': st})
