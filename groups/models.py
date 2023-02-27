import datetime
from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        db_column='g.name'
    )
    start_date = models.DateField(default=datetime.date.today(), validators=[validate_start_date])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group_description = models.TextField()

    class Meta:
        db_table = 'Oxford'
