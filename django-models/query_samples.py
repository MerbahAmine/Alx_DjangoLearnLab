from .models import Author, Book, Librarian, Library

author="Amin"
try :
    author_name = Author.objects.get(name = author)
    all_books = Book.filter(author = author_name)
    print(f"books by {author} are {[book.title for book in all_books]}")

except  Author.DoesNotExist:
        print(f"the author {author} not found")
lib = "ALger"
try: 
   library = Library.objects.get(name = lib)
   books_in_lib = Library.books.all() 
   print(f"all books are{[book.name for book in books_in_lib]}")
except Book.DoesNotExist:
        print(f"the author {Book} not found")


try:
     retrived_librarian = Librarian.objects.get(Library__name = lib)
     print(f"librirain{retrived_librarian.name}")
except Librarian.DoesNotExist:
      print(f"the author {lib} not found")
 
