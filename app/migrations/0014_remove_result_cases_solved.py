# Generated by Django 3.0.2 on 2020-02-25 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_result_cases_solved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='Cases_Solved',
        ),
    ]