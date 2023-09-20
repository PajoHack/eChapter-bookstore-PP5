from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NkkeuB9ngM35Liw3rltSriXWCEizgtd5aVTRDAlwKNrqyl8hXybfei4U9LaWpB37wKY3nJFInIYfASCk0FddiAw00NMv5VZHL',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)