from django.urls import path

from .views import BookView, HomeView, \
    AuthorView, BookDetailView, AuthorDetailView, AuthorBooksDetailView, AddBookView, AddAuthorView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/', BookView.as_view(), name='book_list'),
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/author/<int:pk>', AuthorDetailView.as_view(), name='author_book'),
    path('books/author/author_book/<int:author_index>', AuthorBooksDetailView.as_view(), name='books_author'),
    path('add_book/', AddBookView.as_view(), name="add_book"),
    path('add_author/', AddAuthorView.as_view(), name="add_author")
]
