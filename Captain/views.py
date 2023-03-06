from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Jarvis(request):
    return HttpResponse("<h1>It's Jarvis please help me, This Vision is Destroying me, Avengers be like: No we are busy in drinking and Enjoying Party some are busy at lifting Thore Hammer bye bye</h1>")

def Vision(request):
    return HttpResponse("<h1> I will never leave u Jarvis, They will never stop me HAHAHAHA</h1>")