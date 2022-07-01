from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book
from .forms import BookForm, AuthorForm


def index(request: HttpRequest):
    return render(request, 'bookstore/index.html')


def home(request: HttpRequest):
    return render(request, 'bookstore/home.html')


def book_list(request: HttpRequest):
    books = Book.objects.all().order_by('-id')
    if request.method == 'GET' and 'search' in request.GET:
        search = request.GET['search']
        books = Book.objects.filter(book_title__icontains=search).order_by('-id')

    context = {'books': books}
    return render(request, 'bookstore/book_list.html', context=context)


def author_list(request: HttpRequest):
    authors = Author.objects.all().order_by('-id')
    if request.method == 'GET' and 'search' in request.GET:
        search = request.GET['search']
        authors = Author.objects.filter(first_name__icontains=search).order_by('-id')

    context = {'authors': authors}
    return render(request, 'bookstore/author_list.html', context=context)


def book_detail(request: HttpRequest, book_index):
    book = get_object_or_404(Book, pk=book_index)
    context = {'book': book}
    return render(request, 'bookstore/book_detail.html', context=context)


def author_book(request: HttpRequest, author_index):
    author = get_object_or_404(Author, pk=author_index)
    context = {
        'author': author
    }
    return render(request, 'bookstore/author_book.html', context=context)


def books_author(request: HttpRequest, author_index):
    books = Book.objects.all()
    context = {
        'author': author_index,
        "books": books
    }
    return render(request, 'bookstore/books_author.html', context=context)


def add_book(request: HttpRequest):
    if request.method == "POST":
        form_book = BookForm(request.POST)
        if form_book.is_valid():
            form_book.save()
            return redirect("book_list")
    else:
        form_book = BookForm()
    context = {"form_book": form_book}
    return render(request, "bookstore/add_book.html", context)


def add_author(request: HttpRequest):
    if request.method == "POST":
        form_author = AuthorForm(request.POST)
        if form_author.is_valid():
            form_author.save()
            return redirect("author_list")
    else:
        form_author = AuthorForm()
    context = {"form_author": form_author}
    return render(request, "bookstore/add_author.html", context)
