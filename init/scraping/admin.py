from django.contrib import admin
from .models import City, Language, Vacancy
# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('ct_name', 'ct_slug')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lan_name','lan_slug')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacan_title', 'vacan_company',
                    'vacan_language', 'vacan_city',
                    'vacan_experience', 'vacan_format')
    list_filter = ('vacan_company', 'vacan_language',
                   'vacan_city', 'vacan_experience')
    list_per_page = 50
    list_max_show_all = 100
    search_fields = ('vacan_company','vacan_language',)
    fields = ('vacan_title', 'vacan_language', 'vacan_company',
               'vacan_city', 'vacan_experience', 'vacan_salary',
                'vacan_format', 'vacan_description', 'vacan_url',
               )
