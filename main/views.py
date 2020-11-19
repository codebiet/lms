from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def books(request):
    return HttpResponse("<h1>Books Page</h1>")

def pdfs(request):
    return HttpResponse("<h1>PDFs Page</h1>")

def authenticate(request):
    return HttpResponse("<h1>SignUp/Login Page</h1>")
