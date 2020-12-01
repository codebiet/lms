from django.contrib import admin
from main.models import book, pdf, issued_book, Tag

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'name', 'author', 'publication', 'edition', 'description')

class PDFsAdmin(admin.ModelAdmin):
    list_display = ('id','pdf_file','image', 'name', 'author', 'publication', 'edition', 'description')

class IssuedBooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'book', 'date_issued', 'last_date')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(book, BooksAdmin)
admin.site.register(pdf, PDFsAdmin)
admin.site.register(issued_book, IssuedBooksAdmin)
admin.site.register(Tag, TagAdmin)


