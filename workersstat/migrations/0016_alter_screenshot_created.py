# Generated by Django 4.2.7 on 2024-06-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workersstat', '0015_alter_session_get_screenshots_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='created'),
        ),
    ]