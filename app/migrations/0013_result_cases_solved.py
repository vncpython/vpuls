# Generated by Django 3.0.2 on 2020-02-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200224_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Cases_Solved',
            field=models.CharField(default=123, max_length=300),
            preserve_default=False,
        ),
    ]