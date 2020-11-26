from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import book, pdf
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from account.models import Account



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
                user = form.save()
                email = form.cleaned_data.get('email')
                messages.success(request, "Account was created for " + 'email')

                return redirect('login')
        context = {'form': form}
        return render(request, 'main/signup.html', context)

def loginPg(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email = email, password = password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Email OR Password is incorrect')

        return render(request, 'main/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
