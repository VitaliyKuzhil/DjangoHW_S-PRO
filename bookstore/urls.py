from django.urls import path

from .views import book_list, book_detail, author_book, books_author, add_book, author_list, add_author, home

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('authors/', author_list, name='author_list'),
    path('books/<int:book_index>/', book_detail, name='book_detail'),
    path('books/author/<int:author_index>', author_book, name='author_book'),
    path('books/author/book/<int:author_index>', books_author, name='books_author'),
    path('add_book/', add_book, name="add_book"),
    path('add_author/', add_author, name="add_author")
]
