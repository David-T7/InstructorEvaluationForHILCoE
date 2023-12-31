# Generated by Django 4.2.7 on 2023-11-18 16:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('Criteria_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CriteriaSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationCriteria',
            fields=[
                ('Criteria_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Evaluator', models.CharField(choices=[('Student', 'Student'), ('Instructor', 'Instructor'), ('StaffMember', 'StaffMember')], max_length=255, null=True)),
                ('Evaluatee', models.CharField(choices=[('Lecture Insructor', 'Lecture Insructor'), ('Lab Instructor', 'Lab Instructor')], max_length=255, null=True)),
                ('Criteria_data', models.ManyToManyField(to='Evaluation.criteria')),
            ],
        ),
        migrations.AddField(
            model_name='criteria',
            name='Section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.criteriasection'),
        ),
    ]
