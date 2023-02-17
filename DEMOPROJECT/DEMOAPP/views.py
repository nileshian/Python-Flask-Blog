from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    #return HttpResponse('<h1>This is my home</h1>')
    return render(request,'DEMOAPP/hi.html')