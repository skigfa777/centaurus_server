# Generated by Django 4.2.7 on 2024-06-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workersstat', '0005_alter_screenshot_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='get_screenshots',
            field=models.BooleanField(default=False, verbose_name='Получать скриншоты рабочего стола'),
        ),
    ]