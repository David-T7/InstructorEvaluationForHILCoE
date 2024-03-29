# Generated by Django 4.2.7 on 2024-03-01 10:57

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0027_course_department_alter_term_evaluation_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstructor',
            name='Department',
        ),
        migrations.AlterField(
            model_name='course',
            name='Department',
            field=models.CharField(blank=True, choices=[(None, 'Select Department'), ('Computer Science', 'Computer Science'), ('Software Engineering', 'Software Engineering'), ('Common Course', 'Common Course')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='term',
            name='Evaluation_End_Date',
            field=models.DateTimeField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2024, 3, 1, 10, 57, 47, 316118, tzinfo=datetime.timezone.utc))]),
        ),
        migrations.AlterField(
            model_name='term',
            name='Evaluation_Start_Date',
            field=models.DateTimeField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2024, 3, 1, 10, 57, 47, 316118, tzinfo=datetime.timezone.utc))]),
        ),
    ]
