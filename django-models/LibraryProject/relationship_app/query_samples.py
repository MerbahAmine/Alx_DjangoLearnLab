# query_samples.py

from relationship_app.models import Book, Author, Library, Librarian

# 1. Query all books by a specific author 
author_name = "Merbah Amine"
try:
    author = Author.objects.get(name=author_name)
    all_books = Book.objects.filter(author=author)
    print(f"Books by {author_name}: {[book.title for book in all_books]}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a specific library 
library_name = "City"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a specific library 
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library {library_name}")

