from django.db import models
import datetime

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f.name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l.name')
    birth_date = models.DateField(default=datetime.date.today())
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'Teachers'

    def str(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            t = cls()  # t = Teacher
            t.first_name = f.first_name()
            t.last_name = f.last_name()
            t.birth_date = f.date_between(start_date='-45y', end_date='-25y')
            t.salary = f.random_int(min=20000, max=50000)
            t.save()
