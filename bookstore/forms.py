from django import forms
from django.utils.translation import gettext_lazy as _
from bookstore.models import Book, Author, Review


class BookForm(forms.ModelForm):
    book_title = forms.CharField(max_length=50,
                                 label='Назва книжки',
                                 widget=forms.TextInput(attrs={'class': 'form-control'})
                                 )
    book_description = forms.CharField(label='Опис книжки',
                                       widget=forms.Textarea(attrs={'class': 'form-control', "rows": 3})
                                       )
    released_year = forms.IntegerField(label='Рік видавництва',
                                       max_value=9999,
                                       widget=forms.TextInput(attrs={'class': 'form-control'})
                                       )

    class Meta:
        model = Book
        fields = ['book_title', 'book_description', 'released_year', 'author']
        labels = {
            'author': _('Автор')
        }
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'})
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_description']


class AuthorForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,
                                 label='Імя автора',
                                 widget=forms.TextInput(attrs={'class': 'form-control'})
                                 )
    last_name = forms.CharField(max_length=50,
                                label='Фамілія автора',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    about_author = forms.CharField(label='Біографія',
                                   widget=forms.Textarea(attrs={'class': 'form-control', "rows": 3})
                                   )

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'about_author']
