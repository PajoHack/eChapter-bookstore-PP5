from django.shortcuts import render
from .models import Book

# Create your views here.

def all_products(request):
    """ A view to show all books """

    books = Book.objects.all()  # Query all records from the Book model

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)
