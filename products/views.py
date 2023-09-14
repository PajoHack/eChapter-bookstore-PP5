from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book

# Create your views here.

def all_products(request):
    """ A view to show all books """

    books = Book.objects.all()  # Query all records from the Book model
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(ISBN__icontains=query) | Q(author__name__icontains=query) 
            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """
    
    book = get_object_or_404(Book, pk=book_id)  # Query the Book model

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
