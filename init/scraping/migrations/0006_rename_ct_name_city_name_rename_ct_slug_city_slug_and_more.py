# Generated by Django 4.2 on 2024-11-06 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_remove_vacancy_vacan_savary_vacancy_vacan_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='ct_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='ct_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='lan_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='lan_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_experience',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_format',
            new_name='format',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_salary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_timestamp',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacan_url',
            new_name='url',
        ),
    ]
