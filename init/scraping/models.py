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
