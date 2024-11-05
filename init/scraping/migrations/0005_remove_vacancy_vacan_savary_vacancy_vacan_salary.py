# Generated by Django 4.2 on 2024-11-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_vacancy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='vacan_savary',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='vacan_salary',
            field=models.CharField(blank=True, default='Не указано', max_length=12, verbose_name='Заработная плата'),
        ),
    ]