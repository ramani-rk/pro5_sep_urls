from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def dhoni(request):
    return render(request,'dhoni.html')


def jaddu(request):
    return HttpResponse('<h1><center>Jaddu is the Best All-rounder in CSK </center></h1>')