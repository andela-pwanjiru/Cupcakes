from django import forms

from models import Book, Category


class BookSearchForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'category', )