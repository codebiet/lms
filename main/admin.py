from django.contrib import admin
from main.models import book, pdf

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'name', 'author', 'publication', 'edition', 'description')

class PDFsAdmin(admin.ModelAdmin):
    list_display = ('id','pdf_file','image', 'name', 'author', 'publication', 'edition', 'description')

admin.site.register(book, BooksAdmin)
admin.site.register(pdf, PDFsAdmin)


