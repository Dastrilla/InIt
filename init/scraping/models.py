from django.db import models
from .utils import cyrillic_to_english

# Create your models here.

class City(models.Model):
    ct_name = models.CharField(max_length=150,
                               unique=True,
                               verbose_name="Название населенного пункта")
    ct_slug = models.SlugField(unique=True,
                               blank=True,
                               verbose_name="Ссылка")

    def __str__(self):
        return self.ct_name

    def save(self, *args, **kwargs):
        if not self.ct_slug:
            self.ct_slug = cyrillic_to_english(self.ct_name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'


class Language(models.Model):
    lan_name = models.CharField(max_length=50,
                                unique=True,
                                verbose_name="Язык программирования")
    lan_slug = models.SlugField(unique=True,
                                blank=True,
                                verbose_name='Ссылка')
    
    def __str__(self):
        return self.lan_name

    def save(self, *args, **kwrags):
        if not self.lan_slug:
            self.lan_slug = cyrillic_to_english(self.lan_name)
        super().save()
    
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

class Vacancy(models.Model):
    vacan_url = models.URLField(unique=True, verbose_name='Ссылка на вакансию')
    vacan_title = models.CharField(max_length=100, verbose_name='Название вакансии')
    vacan_company = models.CharField(max_length=100, verbose_name='Компания')
    vacan_description = models.TextField(verbose_name='Описание вакансии')
    vacan_savary = models.IntegerField(blank=True, verbose_name='Заработная плата', default='Не указано')
    vacan_language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')
    vacan_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    vacan_format = models.CharField(max_length=300, verbose_name='Формат работы', default='Офис')
    vacan_experience = models.CharField(max_length=50, blank=True, verbose_name='Опыт', default='Без опыта')
    vacan_timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.vacan_title