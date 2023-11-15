from mi.views import *

from django.urls import path

app_name='someeeething'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('polly/',polly,name='polly'),
]