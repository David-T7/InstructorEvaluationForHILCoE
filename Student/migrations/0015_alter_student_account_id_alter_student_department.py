# Generated by Django 4.2.7 on 2024-03-13 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0014_alter_student_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Account_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='Department',
            field=models.CharField(blank=True, choices=[(None, 'Select Department'), ('Computer Science', 'Computer Science'), ('Software Engineering', 'Software Engineering')], max_length=20, null=True),
        ),
    ]
