from django.shortcuts import render
from apps.settings.models import Geeks, About, Why, Benefits, Count, Works
# Create your views here.
def index(request):
    geeks = Geeks.objects.latest("id")
    about = About.objects.latest('id')
    why = Why.objects.latest("id")
    benefits = Benefits.objects.all()
    count = Count.objects.latest("id")
    works = Works.objects.all()
    return render(request, 'index.html', locals())