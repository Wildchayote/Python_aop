from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def say_hello(request):
    #return HttpResponse('Hello Middlesbrough!\n You alright?')
    me =1
    you =2
    x = ['name']
    y = ['Nigeria!']
    dic = dict(zip(x,y))
    return render(request, 'hello.html',dic)
