from csk.views import *

from django.urls import path

app_name='anything'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('jaddu/',jaddu,name='jaddu'),
]