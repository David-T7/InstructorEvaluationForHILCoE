# Generated by Django 4.2.7 on 2023-11-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0006_alter_peerevaluationresult_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffevaluationresult',
            name='CourseType',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
