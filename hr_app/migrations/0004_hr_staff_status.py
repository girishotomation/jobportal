# Generated by Django 5.0 on 2023-12-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0003_alter_candidateapplication_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='staff_status',
            field=models.BooleanField(default=False),
        ),
    ]
