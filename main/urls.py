from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth import views as auth_views



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
    path('upload_pdf/', views.upload_pdf, name="upload_pdf"),
    path('issue/<str:bid>/', views.issue_book, name="issue_book"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('update_profile/cropImage', views.crop_image, name="crop_image"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),
]

