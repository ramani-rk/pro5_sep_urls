from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')

def faf(request):
    return  HttpResponse('<h1>faf is really fabulous</h1>')