# Generated by Django 4.2 on 2024-11-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Город'},
        ),
        migrations.AlterField(
            model_name='city',
            name='ct_name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='city',
            name='ct_slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Ссылка'),
        ),
    ]
