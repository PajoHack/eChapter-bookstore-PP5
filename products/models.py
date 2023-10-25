from django.db import models

# Create your models here.


class Category(models.Model):

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
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
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
