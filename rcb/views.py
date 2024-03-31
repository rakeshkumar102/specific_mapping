from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'virat.html')

def kartik(request):
    return HttpResponse('<h1> <center> Kartik is match finisher of RCB </center></h1>')