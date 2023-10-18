
from django.shortcuts import render, redirect
from .forms import BMIForm
from .models import BMIRecord
import math



def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi_record = form.save()
            return redirect('bmi_result', pk=bmi_record.pk)
    else:
        form = BMIForm()
    return render(request, 'calculate_bmi.html', {'form': form})

def bmi_result(request, pk):
    bmi_record = BMIRecord.objects.get(pk=pk)
    name = bmi_record.name
    height = bmi_record.height
    weight = bmi_record.weight
    bmi = round((weight / (height ** 2)),2)
    
    bmi_result = BMIRecord(name=name, weight=weight, height=height, BMI=bmi)
    bmi_result.save()
    
    if pk%2 !=0:
        BMIRecord.objects.get(pk=pk).delete()
    return render(request, 'bmi_result.html', {'bmi_record': bmi_record, 'bmi': bmi, 'bmi_result': bmi_result})

