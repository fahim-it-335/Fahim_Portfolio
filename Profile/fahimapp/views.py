from django.shortcuts import render
from django.http import HttpResponse
from fahimapp.models import Contract

# Create your views here.

def home(request):
    return render(request, 'index.html')

def project_1(request):
    return render(request, 'project_1.html')

def project_2(request):
    return render(request, 'project_2.html')

def project_3(request):
    return render(request, 'project_3.html')

def contract(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        values = Contract(name=name, email=email, subject=subject, message=message)
        values.save()
    return render(request, 'return.html')
