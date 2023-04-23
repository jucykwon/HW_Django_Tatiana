from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.fields import Str
from webargs.djangoparser import use_args

from teachers.forms import CreateTeacherForm, UpdateTeacherForm, FilterTeacherForm
from teachers.models import Teacher


def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)
def get_teachers(request, args):
    teachers = Teacher.objects.all().order_by('birth_date')
    filter_form = FilterTeacherForm(data=request.GET, queryset=teachers)
    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'filter_form': filter_form,
        }
    )


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'title': 'Detail of teacher', 'teacher': teacher})


def create_teacher_view(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/create.html', {'form': form})


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/update.html', {'form': form})

    return HttpResponse(html_form)


def delete_teacher(request, pk):
    st = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    if request.method == 'GET':
        return render(request, 'teachers/delete.html', {'teacher': st})
