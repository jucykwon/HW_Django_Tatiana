# Generated by Django 4.1.7 on 2023-04-24 00:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
import groups.validators


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_start_date'),
        ('groups', '0010_group_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='active_course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_group', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='group',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 4, 24), validators=[groups.validators.validate_start_date]),
        ),
    ]
