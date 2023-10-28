from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Category model for representing book categories in the online bookstore.
    
    Fields:
        - name (CharField): The name of the category.
        - friendly_name (CharField): A more human-friendly name of the category, can be null.
        - description (TextField): A description of the category.
    """
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Author(models.Model):
    """
    Author model for representing book authors in the online bookstore.
    """
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model for representing books in the online bookstore.

    Fields:
        - title (CharField): The title of the book.
        - author (ForeignKey): A foreign key to the Author model, can be null.
        - ISBN (CharField): The ISBN number of the book, can be null.
        - publisher (CharField): The publisher of the book, can be null.
        - price (DecimalField): The price of the book.
        - category (ForeignKey): A foreign key to the Category model, can be null.
        - cover_image (ImageField): The cover image of the book, can be null.
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'Author', null=True, blank=True, on_delete=models.SET_NULL)
    ISBN = models.CharField(max_length=13, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    cover_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
