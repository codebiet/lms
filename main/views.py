from django.shortcuts import render
from django.http import HttpResponse
from main.models import book, pdf

def index(request):
    return render(request, 'main/index.html')

def book_col(request):
    book_display = book.objects.all()
    return render(request, 'main/book.html', {'book':book_display})

def pdf_col(request):
    pdf_display = pdf.objects.all()
    return render(request, 'main/pdf.html', {'pdf':pdf_display})

def authenticate(request):
    return HttpResponse("<h1>SignUp/Login Page</h1>")
