```
Podstawowa klasa biblioteki

Założenia:
Szablon który indeksuje elementy ksiązki używająć zależności tabeli (self.books)
oraz pozwala na wywołanie oraz wyświetlenie informacji z ksiązki.
```

class Library:
    def __init__ (self):
        self.books = []
    def add_book (self, book):
        self.books.append(book)
    def display_books (self):
        for book in self.books:
            print(f"{book.title} by {book.author}")
