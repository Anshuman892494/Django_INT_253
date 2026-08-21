from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Homepage!</h1>")

def about(request):
    return HttpResponse("<h1>About Us Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us Page</h1>")

def services(request):
    return HttpResponse("<h1>Our Services Page</h1>")

def result(request, marks=85):
    if marks >= 80:
        grade = "Excellent"
    elif marks >= 60:
        grade = "Good"
    elif marks >= 40:
        grade = "Average"
    else:
        grade = "Fail"
    return HttpResponse(f"<h1>Marks: {marks}</h1><h2>Result: {grade}</h2>")

