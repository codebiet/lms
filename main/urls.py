from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books, name = "books"),
    path('pdfs/', views.pdfs, name = "pdfs"),
    path('authenticate/', views.authenticate, name = "authenticate"),
]