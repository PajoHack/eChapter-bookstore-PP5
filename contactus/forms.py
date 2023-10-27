from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A form for handling contact inquiries.

    This form is linked to the Contact model and includes fields for 
    the name, email, subject, and message of the inquiry.
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
