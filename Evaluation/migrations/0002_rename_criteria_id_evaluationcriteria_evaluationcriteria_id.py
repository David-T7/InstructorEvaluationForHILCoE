# Generated by Django 4.2.7 on 2023-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluationcriteria',
            old_name='Criteria_id',
            new_name='EvaluationCriteria_id',
        ),
    ]
