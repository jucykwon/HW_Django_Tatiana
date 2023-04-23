import datetime
from django.db import models
from faker import Faker
import iso639

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

    def __str__(self):
        return f'{self.group_name} {self.start_date}'

    @classmethod
    def generate_fake_group(cls, cnt):
        f = Faker()
        names = ('Polish', 'Swedish', 'Danish', 'Hindi', 'Portuguese', 'Cantonese', 'Vietnamese', 'Turkish', 'Korean',
                 'German', 'Italian', 'French', 'Spanish', 'Japanese', 'Chinese', 'Thai', 'Greek', 'Danish', 'Irish')
        existing_names = list(cls.objects.values_list('group_name', flat=True))
        for p in range(cnt):
            name = f.random.choice(names)
            while name in existing_names:
                p += 1
                name = f'{name}_{p}'
            g = cls()
            g.group_name = name
            g.start_date = f.date_this_year()
            g.group_description = f.text()
            g.save()
