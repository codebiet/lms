from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from main.models import book, pdf, issued_book
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from account.models import Account
from django.db.models import Q


def get_queryset(request, query):
    querysetbook = []
    querysetpdf = []
    #print('query=', query)
    queries = query.split(" ")
    for q in queries:
        docbooks = book.objects.filter(
            Q(name__icontains=q) |
            Q(author__icontains=q) |
            Q(publication__icontains=q) |
            Q(edition__icontains=q) |
            Q(description__icontains=q)
        ).distinct()
        for docbook in docbooks:
            querysetbook.append(docbook)
        docpdfs = pdf.objects.filter(
            Q(name__icontains=q) |
            Q(author__icontains=q) |
            Q(publication__icontains=q) |
            Q(edition__icontains=q) |
            Q(description__icontains=q)
        ).distinct()
        for docpdf in docpdfs:
            querysetpdf.append(docpdf) 
    
    return list(set(querysetbook)), list(set(querysetpdf))

def index(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)
        
    return render(request, 'main/index.html')

def book_col(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)

    book_display = book.objects.all()
    paginator = Paginator(book_display, 1)

    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    context = {'page_obj' : page_obj}
    return render(request, 'main/book.html', context)


def pdf_col(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)

    pdf_display = pdf.objects.all()
    paginator = Paginator(pdf_display, 1)

    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    context = {'page_obj' : page_obj}
    return render(request, 'main/pdf.html', context)

def book_pg(request, book_id):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)

    bk_pg = book.objects.get(id=book_id)
    context = {'bk_pg' : bk_pg}
    return render(request, 'main/specific_book.html', context)

def pdf_pg(request, pdf_id):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)

    p_pg = pdf.objects.get(id=pdf_id)
    context = {'p_pg' : p_pg}
    return render(request, 'main/specific_pdf.html', context)

def signup(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)

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
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)

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

@login_required(login_url='login')
def profile(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)
    
    return render(request, 'main/profile.html')

@login_required(login_url='issued_books')
def issued_books(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        #print(query)
        qsetbook, qsetpdf = get_queryset(request, query)
        context = {'qsetbook': qsetbook, 'qsetpdf': qsetpdf}
        return render(request, 'main/search_related.html', context)
        
    user = request.user
    orders = issued_book.objects.filter(account = user.id)
    context = {'orders': orders}
    return render(request, 'main/issuedbook.html',context)


    