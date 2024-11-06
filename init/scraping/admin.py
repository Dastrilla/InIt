from django.contrib import admin
from .models import City, Language, Vacancy
# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company',
                    'language', 'city',
                    'experience', 'format')
    list_filter = ('company', 'language',
                   'city', 'experience')
    list_per_page = 50
    list_max_show_all = 100
    search_fields = ('company','language',)
    fields = ('title', 'language', 'company',
               'city', 'experience', 'salary',
                'format', 'description', 'url',
               )
