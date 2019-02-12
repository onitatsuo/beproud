from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from fruit.models import Master
from django.views.generic.list import ListView


def index(request):
    return render(request, 'fruit/index.html')

@login_required(login_url='/login')
def top(request):
    return render(request, 'fruit/top.html')

def master(request):
    return render(request, 'fruit/master.html')

def jouhou(request):
    return render(request, 'fruit/jouhou.html')

def toukei(request):
    return render(request, 'fruit/toukei.html')

def add(request):
    return render(request, 'fruit/add.html')

def models(request):
    query_results = Master.objects.all()
    return render(request, 'fruit/master.html', {'query_results':query_results})



#def models(reuqest):
#    fruit_name = Master.objects.all()
#    fruit_price = Master.objects.all()
#    fruit_date = Master.objects.all()
