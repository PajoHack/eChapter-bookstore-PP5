from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
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
