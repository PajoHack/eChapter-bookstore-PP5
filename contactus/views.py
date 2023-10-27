from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """  A view to handle the contact us form submission """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): # Validates the form data
            form.save() # Saves the form data to the database
            messages.success(
                request,
                (
                    'Your message was sent successfully.'
                    'We will be in touch shortly.'
                )
            )
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contactus/contact_us.html', {'form': form})
