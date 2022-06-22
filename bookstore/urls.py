from django.urls import path

from .views import book_list, book_detail, author_book, books_author

urlpatterns = [
    path('', book_list, name='book_list'),
    path('books/<int:book_index>/', book_detail, name='book_detail'),
    path('books/author/<int:author_index>', author_book, name='author_book'),
    path('books/author/book/<int:author_index>', books_author, name='books_author')
]
