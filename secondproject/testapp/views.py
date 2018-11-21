from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your view hereself.

def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>hello friend good evening!!!</h1><hr>'
    msg=msg+"<h1>now server time is:"+str(date)+"</h1>"
    return HttpResponse(msg)
