from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import book, pdf
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def book_col(request):
    book_display = book.objects.all()
    return render(request, 'main/book.html', {'book':book_display})

def pdf_col(request):
    pdf_display = pdf.objects.all()
    return render(request, 'main/pdf.html', {'pdf':pdf_display})

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)

                return redirect('login')

        return render(request, 'main/signup.html', {'form':form})

def loginPg(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        return render(request, 'main/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
