from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from students.models import Student
from .forms import UpdateGroupForm, CreateGroupForm, FilterGroupForm
from .models import Group

from webargs.fields import Str
from webargs.djangoparser import use_args


def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'group_name': Str(required=False),
        'start_date': Str(required=False),
    },
    location='query',
)
def get_groups(request, args):
    groups = Group.objects.all().order_by('group_name')
    filter_form = FilterGroupForm(data=request.GET, queryset=groups)
    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'filter_form': filter_form,
        }
    )


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'title': 'Detail of group', 'group': group})


def create_group_view(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/create.html', {'form': form})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'POST':
        form = UpdateGroupForm(data=request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = UpdateGroupForm(instance=group, initial=students)
    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, pk):
    st = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    if request.method == 'GET':
        return render(request, 'groups/delete.html', {'group': st})
