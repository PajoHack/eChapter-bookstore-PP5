from django import forms
from .widgets import CustomClearableFileInput
from .models import Book


class BookForm(forms.ModelForm):
    """
    Form class for creating and updating Book instances in the online bookstore.

    Inherits from:
        - forms.ModelForm

    Attributes in Meta Class:
        - model: Specifies the model to use, which is 'Book'.
        - fields: Specifies which fields to include in the form, using '__all__' to include all fields.

    Fields:
        - cover_image: Overridden to use a custom widget and label.

    Methods:
        - __init__: Initializes form fields and applies CSS classes.
    """
    class Meta:
        model = Book
        fields = '__all__'

    # Overriding the cover_image field to utilize a custom widget and change label
    cover_image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
