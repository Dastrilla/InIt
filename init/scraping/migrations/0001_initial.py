# Generated by Django 4.2 on 2024-11-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ct_name', models.CharField(max_length=150)),
                ('ct_slug', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
