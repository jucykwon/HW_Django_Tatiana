from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from .forms import UpdateGroupForm, CreateGroupForm
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
    if len(args) and (args.get('group_name') or args.get('start_date')):
        groups = groups.filter(
            Q(group_name=args.get('group_name', '')) | Q(start_date=args.get('start_date', ''))
        )
    return render(
        request=request,
        template_name='groups/list.html',
        context={'title': 'List of groups', 'groups': groups}
    )


def detail_group(request, pk):
    group = Group.objects.get(pk=pk)
    return render(request, 'groups/detail.html', {'title': 'Detail of group', 'group': group})


def create_group_view(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
        <input type="submit" value="Submit"><br><br>
        <a href="/groups/"> Back to list</a>
        </form> 
        '''

    return HttpResponse(html_form)


def update_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
        <input type="submit" value="Submit"><br><br>
        <a href="/groups/">Back to List</a>
        </form> 
        '''

    return HttpResponse(html_form)
