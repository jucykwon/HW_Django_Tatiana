# Generated by Django 4.1.7 on 2023-04-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_group_headman'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
