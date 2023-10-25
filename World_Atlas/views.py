from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import AtlasForm
from . models import Nation
import json



def country_form(request):
    if request.method == 'POST':
        form = AtlasForm(request.POST)
        if form.is_valid():
            nation_record = form.save()
            return redirect('get_capital', pk=nation_record.pk)
    else:
        form = AtlasForm()
    return render(request, 'country.html', {'form': form})

def get_capital(request,pk):
    nation_record = Nation.objects.get(pk=pk)
    with open('dictionary.txt', 'r') as file:
        world_atlas = json.load(file)                                       # dictionary
    nation = nation_record.nation.lower()
    
    if nation in world_atlas:
        capital =  world_atlas[nation].upper()
    else:
        error = f'not found. Check spelling and try again!'
        capital =  error

    nation = nation_record.nation.title()
    nation_capital = Nation(nation=nation, capital = capital)
    nation_capital.save()

    if pk%2 != 0:
        Nation.objects.get(pk=pk).delete()  
    context = {'nation_record': nation_record, 'capital': capital}
    return render(request, 'capital.html', context)
