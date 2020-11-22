from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index , name="index"),
    path('books/', views.book_col, name = "books"),
    path('pdfs/', views.pdf_col, name = "pdfs"),
    path('authenticate/', views.authenticate, name = "authenticate"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)