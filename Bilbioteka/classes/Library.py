```
Podstawowa klasa biblioteki

Założenia:
Szablon który indeksuje elementy ksiązki używająć zależności tabeli (self.books)
oraz pozwala na wywołanie oraz wyświetlenie informacji z ksiązki.
```
from database import get_connection
from classes.Book import Book

class Library:
    def add_book (self, book):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (book.title, book.author)   
        )
        
        conn.commit()
        commit.close()

    def display_books (self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        for row in rows:
            book - Book(row["title"], row["author"], row["id"])
            print(f"{book.id}.{book.title} by {book.author}")

    conn.close()
