from django.shortcuts import render

from . models import Place
from . models import Team

def sample2(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()

    return render (request,"index.html",{'result':obj , 'result2':obj2})

# Create your views here.
