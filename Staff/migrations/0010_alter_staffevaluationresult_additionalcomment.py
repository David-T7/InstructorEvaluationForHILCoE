# Generated by Django 4.2.7 on 2023-12-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0009_staffevaluationresult_additionalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffevaluationresult',
            name='AdditionalComment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
