from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('', views.index , name="index"),
    path('books/', views.book_col, name = "books"),
    path('pdfs/', views.pdf_col, name = "pdfs"),
    path('signup/', views.signup, name = "register"),
    path('login/', views.loginPg, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('books/book/<str:book_id>/', views.book_pg, name = "book"),
    path('pdfs/pdf/<str:pdf_id>/', views.pdf_pg, name = "pdf"),
    path('profile/', views.profile, name= "profile"),
    path('issued_books/', views.issued_books, name="issued_books"),
    path('search_results/', views.get_queryset, name="search"),
]

