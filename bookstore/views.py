from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.urls import reverse_lazy

from .models import Author, Book, Review
from .forms import BookForm, AuthorForm, ReviewForm
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import FormView


class IndexView(TemplateView):
    template_name = 'bookstore/index.html'


class HomeView(TemplateView):
    template_name = 'bookstore/home.html'


class BookView(View):
    def post(self, request: HttpRequest):
        books = Book.objects.all().order_by("-id")
        context = {
            "books": books,
        }
        return render(request, "bookstore/book_list.html", context=context)

    def get(self, request: HttpRequest):
        books = Book.objects.all().order_by('-id')
        if request.method == 'GET' and 'search' in request.GET:
            search = request.GET['search']
            books = Book.objects.filter(book_title__icontains=search).order_by('-id')

        context = {'books': books}
        return render(request, 'bookstore/book_list.html', context=context)


class ReviewView(View):
    def post(self, request: HttpRequest, book_index):
        book = get_object_or_404(Book, pk=book_index)
        review = get_list_or_404(Review)
        form = ReviewForm()
        context = {
            'book': book,
            'review': review,
            'form': form
        }
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                description = request.POST.get('review_description')
                form = Review.objects.create(book_id=book, user=request.user, review_description=description)
                form.save()
                return redirect('book', pk=book_index)
        return render(request, 'book_detail.html', context)

    def get(self, request: HttpRequest, book_index):
        book = get_object_or_404(Book, pk=book_index)
        review = get_list_or_404(Review)
        form = ReviewForm()
        context = {
            'book': book,
            'review': review,
            'form': form
        }
        return render(request, 'book_detail.html', context)


class AuthorView(View):
    def post(self, request: HttpRequest):
        authors = Author.objects.all().order_by('-id')
        context = {
            'authors': authors
        }
        return render(request, 'bookstore/author_list.html', context=context)

    def get(self, request: HttpRequest):
        authors = Author.objects.all().order_by('-id')
        if request.method == 'GET' and 'search' in request.GET:
            search = request.GET['search']
            authors = Author.objects.filter(first_name__icontains=search).order_by('-id')

        context = {'authors': authors}
        return render(request, 'bookstore/author_list.html', context=context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'bookstore/book_detail.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'bookstore/author_book.html'


class AuthorBooksDetailView(View):
    def get(self, request: HttpRequest, author_index):
        books = Book.objects.all()
        context = {
            'author': author_index,
            'books': books
        }
        return render(request, 'bookstore/books_author.html', context=context)


class AddBookView(FormView):
    form_class = BookForm
    success_url = reverse_lazy("book_list")
    template_name = "bookstore/add_book.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddAuthorView(FormView):
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")
    template_name = "bookstore/add_author.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
