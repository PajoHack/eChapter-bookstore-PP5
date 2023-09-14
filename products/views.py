from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Category

# Create your views here.

def all_products(request):
    """ A view to show all books, including sorting and search queries """

    books = Book.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':  # Changed from 'name' to 'title'
                sortkey = 'lower_title'
                books = books.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            books = books.order_by(sortkey)  # Now updating the 'books' queryset

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(author__name__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else 'default'

    context = {
        'books': books,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """
    
    book = get_object_or_404(Book, pk=book_id)  # Query the Book model

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
