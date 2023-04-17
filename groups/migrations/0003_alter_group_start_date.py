# Generated by Django 4.1.7 on 2023-03-31 21:08

import datetime
from django.db import migrations, models
import groups.validators


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 3, 31), validators=[groups.validators.validate_start_date]),
        ),
    ]
