from django.urls import path
from . import views

urlpatterns=[
    path("hello/",views.home)
]

def abc(parh,meth):
    meth(response)
    
    
abc("jh/",views.home)    