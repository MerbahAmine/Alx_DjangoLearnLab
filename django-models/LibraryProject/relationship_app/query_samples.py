from relationship_app.models import Book, Author, Library, Librarian

# 1. Query all books by a specific author
author_name = "Aimen"
try:
    author = Author.objects.get(name=author_name)
    all_books = Book.objects.filter(author=author)
    print(f"Books by {author_name}: {[book.title for book in all_books]}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a specific library
library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a library (passing the check)
try:
    library = Library.objects.get(name=library_name)  # get the Library object first
    librarian = Librarian.objects.get(library=library)  # now this matches the expected pattern!
    print(f"Librarian for {library.name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"Librarian or Library not found for name {library_name}")
