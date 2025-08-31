from django.contrib import admin
from .models import Book
# Register your models here.



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns displayed in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters shown on the right sidebar
    list_filter = ('author', 'publication_year')

    # Search bar (searchable fields)
    search_fields = ('title', 'author')
