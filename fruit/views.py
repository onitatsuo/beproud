from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from fruit.models import Master
from django.views.generic.list import ListView
from .forms import DataForm, AddForm


def index(request):
    return render(request, 'fruit/index.html')

@login_required(login_url='/login')
def top(request):
    return render(request, 'fruit/top.html')

@login_required(login_url='/login')
def master(request):
    query_results = Master.objects.all()
    return render(request, 'fruit/master.html', {'query_results':query_results})

@login_required(login_url='/login')
def jouhou(request):
    return render(request, 'fruit/jouhou.html')

@login_required(login_url='/login')
def toukei(request):
    return render(request, 'fruit/toukei.html')

#@login_required(login_url='/login')
#def add(request):
#
#    if request.method == 'POST':
#        form = DataForm(request.POST)
#        if form.is_valid():
#
#            fruit_name = form.cleaned_data('fruit_name')
#            fruit_price = form.cleaned_data('fruit_price')
#
#            print(fruit_name,fruit_price)
#
#
#    form = DataForm()
#    return render(request, 'fruit/add.html', {'form': form})


def add_it(request):

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/master/')


    form = AddForm()
    return render(request, 'fruit/add.html', {'form': form})
