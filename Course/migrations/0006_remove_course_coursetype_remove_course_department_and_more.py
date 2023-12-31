# Generated by Django 4.2.7 on 2023-11-27 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instructor', '0005_alter_instructor_account_id'),
        ('Course', '0005_course_coursetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='CourseType',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Instructors',
        ),
        migrations.CreateModel(
            name='CourseInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseType', models.CharField(blank=True, choices=[(None, 'CourseType'), ('Lecture', 'Lecture'), ('Lab', 'Lab')], max_length=10, null=True)),
                ('Department', models.CharField(blank=True, choices=[(None, 'SelectDepartment'), ('CS', 'CS'), ('SE', 'SE'), ('Both', 'Both')], max_length=10, null=True)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
                ('Instructors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instructor.instructor')),
            ],
        ),
    ]
