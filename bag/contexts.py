from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Book


def bag_contents(request):
    """
    Calculates the contents of the shopping bag, including individual and total prices,
    and the delivery cost if applicable.

    Args:
        request (HttpRequest): The request object to access the session data.

    Returns:
        dict: A dictionary containing the details of the bag contents, including 
              the list of items, total cost, delivery cost, and grand total.
    """
    
    bag_items = []
    total = 0
    book_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        book = get_object_or_404(Book, pk=item_id)
        subtotal = quantity * book.price
        total += quantity * book.price
        book_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
            'subtotal': subtotal
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
