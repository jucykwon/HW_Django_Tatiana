# Generated by Django 4.1.7 on 2023-04-23 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_alter_teacher_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(default=datetime.date(2023, 4, 23)),
        ),
    ]