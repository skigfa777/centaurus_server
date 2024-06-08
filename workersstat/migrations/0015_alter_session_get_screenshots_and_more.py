# Generated by Django 4.2.7 on 2024-06-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workersstat', '0014_alter_session_start_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='get_screenshots',
            field=models.BooleanField(default=False, verbose_name='Получить скриншот рабочего стола (обновите эту страницу ~ через 30 сек после сохранения правки)'),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_activity',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start activity'),
        ),
    ]