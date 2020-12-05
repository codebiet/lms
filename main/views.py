from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from main.models import book, pdf, issued_book
from .forms import CreateUserForm, UploadPdfForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from account.models import Account
from django.db.models import Q
<<<<<<< HEAD
from django.urls import reverse
=======

import nltk
from nltk.corpus import words
from nltk.corpus import wordnet
import numpy as np
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
import pandas
from nltk.corpus import stopwords

correct_spellings = words.words()
spellings_series = pandas.Series(correct_spellings)

def jaccard1(entries, gram_number):

    outcomes = []
    for entry in entries: #iteratively for loop
        if len(entry)>=gram_number:
            spellings = spellings_series[spellings_series.str.startswith(entry[0])]
            distances = ((jaccard_distance(set(ngrams(entry.lower(), gram_number)),
                                           set(ngrams(word.lower(), gram_number))), word)
                         for word in spellings)
            sorted_dist = sorted(distances,reverse=False)
            all_words=[i[1] for i in sorted_dist[:5] ]
            outcomes.append(all_words)
        else:
            outcomes.append(entry)
    return outcomes
>>>>>>> c73bc16b0db1cb625e5fca22a7c41c629714d4ad

def get_queryset(request, query):

    search = query
    entries = search.lower().split()
    output = jaccard1(entries, 2)

    synonyms = []
    all_words=[]
    for words in output:
        for word in words:
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            all_words.append(synonyms)

    word_list=[]
    for i in all_words:
        for j in i:
            word_list.append(j)

    unique_words=np.unique([k.split('_') for k in word_list])

    l=[]
    z=unique_words
    if len(z)>0:
        if type(z[0])==list:
            for words in z:
                for word in words:
                    l.append(word)
        elif type(z[0])==np.str_:
            for words in z:
                l.append(words)

    words=[word for word in l if not word in stopwords.words('english')]

    querysetbook=[]
    querysetpdf=[]

    for q in words:
        docbooks = book.objects.filter(Q(name__icontains=q) |
                    Q(description__icontains=q)
        ).distinct()
        for docbook in docbooks:
            querysetbook.append(docbook)
        docpdfs = pdf.objects.filter(Q(name__icontains=q) |
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

    book_display = book.objects.all()
    paginator = Paginator(book_display, 1)

    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    context = {'page_obj' : page_obj}
    return render(request, 'main/book.html', context)


def pdf_col(request):

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
    user = request.user
    issued = False
    if issued_book.objects.filter(account=user, book=bk_pg).exists():
        issued = True
    context = {'bk_pg' : bk_pg, 'issued' : issued}
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
<<<<<<< HEAD

@login_required(login_url='upload_pdf')
def upload_pdf(request):
    form = UploadPdfForm()
    if request.method == 'POST':
        print(request.POST)
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            print('post:',request.POST)
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'main/upload_pdf.html', context)
    
@login_required(login_url='upload_pdf')
def issue_book(request, bid):
    b = book.objects.get(id = bid)
    user = request.user
    issued= False
    print(b, user)
    if issued_book.objects.filter(account=user, book=b).exists():
        ib = issued_book.objects.get(account=user, book=b)
        print('deleted')
        ib.delete()
        issued = False
    else:
        ib = issued_book.objects.create(account=user, book=b)
        print('saved')
        ib.save()
        issued = True
    return HttpResponseRedirect(reverse('book', args=[str(bid)]))
=======
>>>>>>> c73bc16b0db1cb625e5fca22a7c41c629714d4ad
