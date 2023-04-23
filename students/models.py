import datetime
from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker
from faker.generator import random

from groups.models import Group
from students.validators import ValidateEmailDomains, validate_unique_email

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'hotmail.com')


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name',
                                  validators=[MinLengthValidator(3, message='"First name" field value less than 2 '
                                                                            'symbols')])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name',
                                 validators=[MinLengthValidator(3, message='"Last name" field value less than 2 '
                                                                           'symbols')])
    birthday = models.DateField(default=datetime.date.today(), blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomains(*VALID_DOMAINS), validate_unique_email])
    phone = models.CharField(max_length=13, default=None)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker('uk_UA')
        provider = f.phone_number
        for _ in range(cnt):
            s = cls()  # s = Student
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name}.{s.last_name}@{f.random.choice(VALID_DOMAINS)}'
            s.birthday = f.date_between(start_date='-35y', end_date='-18y')
            s.city = f.city()
            s.phone = provider()
            s.group = random.choice(Group.objects.all())
            s.save()
