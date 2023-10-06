from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page or a 'Thank you' page
    else:
        form = ContactForm()

    return render(request, 'contactus/contact_us.html', {'form': form})

