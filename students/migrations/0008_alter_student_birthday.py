# Generated by Django 4.1.7 on 2023-04-24 00:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_birthday_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(2023, 4, 24)),
        ),
    ]
