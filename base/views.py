from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<b>Welcome to our site</b>")