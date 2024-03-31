from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return render(request,'msd.html')

def ruturaj(request):
    return HttpResponse('<h1> <center>Ruturaj is new Captain of CSK </center></h1>')