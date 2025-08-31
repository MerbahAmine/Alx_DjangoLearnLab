# Retrieve Operation

## Command
```python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.id, book.title, book.author, book.publication_year
# Expected Output:
# (1, '1984', 'George Orwell', 1949)
