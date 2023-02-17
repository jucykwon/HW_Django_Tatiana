import datetime
from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        db_column='g.name'
    )
    start_date = models.DateField(default=datetime.date.today())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group_description = models.TextField()

    class Meta:
        db_table = 'Oxford'
