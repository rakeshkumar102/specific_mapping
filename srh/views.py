from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def klassen(request):
    return render(request,'klassen.html')

def abhishek(request):
    return HttpResponse('<h1> <center> Abhishek Sharma is a attacking opener of SRH </center></h1>')