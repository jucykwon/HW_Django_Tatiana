# Generated by Django 4.1.7 on 2023-03-22 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='f.name', max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(db_column='l.name', max_length=50, verbose_name='Last name')),
                ('birth_date', models.DateField(default=datetime.date(2023, 3, 22))),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
    ]
