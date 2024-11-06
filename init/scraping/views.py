from django.shortcuts import render
from .models import Vacancy
from .forms import FilterForm
# Create your views here.

def index(request):
    form = FilterForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs=[]
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language


        qs = Vacancy.objects.filter(**_filter)
    
    context = {
        'object_list':qs,
        'form': form
    }
    return render(request, 'scraping/index.html', context)