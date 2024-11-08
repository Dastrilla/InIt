# Generated by Django 4.2 on 2024-11-02 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_language_alter_city_options_alter_city_ct_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacan_url', models.URLField(unique=True, verbose_name='Ссылка на вакансию')),
                ('vacan_title', models.CharField(max_length=100, verbose_name='Название вакансии')),
                ('vacan_company', models.CharField(max_length=100, verbose_name='Компания')),
                ('vacan_description', models.TextField(verbose_name='Описание вакансии')),
                ('vacan_savary', models.IntegerField(blank=True, default='Не указано', verbose_name='Заработная плата')),
                ('vacan_format', models.CharField(default='Офис', max_length=300, verbose_name='Формат работы')),
                ('vacan_experience', models.CharField(blank=True, default='Без опыта', max_length=50, verbose_name='Опыт')),
                ('vacan_timestamp', models.DateField(auto_now_add=True)),
                ('vacan_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city', verbose_name='Город')),
                ('vacan_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language', verbose_name='Язык программирования')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
