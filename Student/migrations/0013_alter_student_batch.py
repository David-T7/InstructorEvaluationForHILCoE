# Generated by Django 4.2.7 on 2023-12-04 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0012_alter_term_evaluation_end_date_and_more'),
        ('Student', '0012_alter_studentevaluationresult_additionalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Course.batch'),
        ),
    ]
