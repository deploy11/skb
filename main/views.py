from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import CreateView
# Create your views here.
@login_required(login_url='login')
def home(request):
    fuqorolars = FuqoroMurojat.objects.all().count()
    tashkilotlars = TashkilotMurojat.objects.all().count()
    fuqorolar = FuqoroMurojat.objects.all()
    tashkilotlar = TashkilotMurojat.objects.all()
    context = {
        'fs':fuqorolars,
        'ts':tashkilotlars,
        'fuqorolar':fuqorolar,
        'tashkilotlar':tashkilotlar
    }
    return render(request,'home.html',context)

class Fuqoro(CreateView):
    model = FuqoroMurojat
    fields = '__all__'
    template_name = 'fuqoro.html'

class Tashkilot(CreateView):
    model = TashkilotMurojat
    fields = '__all__'
    template_name = 'tashkilot.html'
      