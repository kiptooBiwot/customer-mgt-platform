from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello from the Django side!')

def accounts(request):
    return HttpResponse('Accounts!')

def customer(request):
    return HttpResponse('Customer Page!')