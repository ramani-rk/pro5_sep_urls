from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def rohit(request):
    return render(request,'rohit.html')


def polly(request):
    return HttpResponse('<center>polly is one of the Best finisher in Mi</center>')