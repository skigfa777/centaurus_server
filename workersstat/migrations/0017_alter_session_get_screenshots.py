# Generated by Django 4.2.7 on 2024-06-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workersstat', '0016_alter_screenshot_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='get_screenshots',
            field=models.BooleanField(default=False, null=True, verbose_name='Получить скриншот рабочего стола (обновите эту страницу ~ через 30 сек после сохранения правки)'),
        ),
    ]
