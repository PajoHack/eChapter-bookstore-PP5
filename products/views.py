from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

def all_products(request):
    """ A view to show all books """

    books = Book.objects.all()  # Query all records from the Book model

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """
    
    book = get_object_or_404(Book, pk=book_id)  # Query the Book model

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
