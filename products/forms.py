from django import forms
from .widgets import CustomClearableFileInput
from .models import Book, Category


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    # Changed from 'image' to 'cover_image' to match the model
    cover_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
