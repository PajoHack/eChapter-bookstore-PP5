from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):  # Renaming to BookForm

    class Meta:
        model = Book  # Using Book model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
