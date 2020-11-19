from django.contrib import admin
from main.models import Book, PDF

class BooksAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'author', 'publication', 'edition', 'description')

class PDFsAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'author', 'publication', 'edition', 'description')

admin.site.register(Book, BooksAdmin)
admin.site.register(PDF, PDFsAdmin)

