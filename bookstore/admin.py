from django.contrib import admin
from .models import Book, Author, Review


class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
    search_fields = ['book_title']
    list_filter = ['book_title', 'author']
    list_editable = ['book_title', 'book_description', 'released_year', 'author']


class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']
    list_editable = ['first_name', 'last_name', 'about_author']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Review)
