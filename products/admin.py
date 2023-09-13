from django.contrib import admin
from .models import Category, Author, Book


# Register your models here.


# Registering the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')

admin.site.register(Category, CategoryAdmin)

# Registering the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Author, AuthorAdmin)

# Registering the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ISBN', 'publisher', 'price', 'category')

admin.site.register(Book, BookAdmin)
