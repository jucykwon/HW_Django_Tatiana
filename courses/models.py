import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from groups.models import Group


class Course(models.Model):
    course_name = models.CharField(
        max_length=50,
        verbose_name='Course name',
        db_column='c.name'
    )
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    course_description = models.TextField()
    is_active = models.BooleanField(_('Is active'), default=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='courses')

    class Meta:
        db_table = 'Course'

    def __str__(self):
        return f'{self.course_name} {self.start_date}'

