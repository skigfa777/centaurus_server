# Generated by Django 4.2.7 on 2024-06-05 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workersstat', '0010_rename_employersession_employeesession'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeSession',
            new_name='Session',
        ),
    ]
