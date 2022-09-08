from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm


def welcomepage(request):
    return  HttpResponse("App is installed and linked ")
# Create your views here.

def home_page(request):
    context ={}
    context['text'] = InputForm()
    return render(request,"Home.html",context)



