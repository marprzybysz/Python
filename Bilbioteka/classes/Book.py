```
Podstawowa klasa książki

Założenia:
Szablon który zawiera informacje ksiązki (autor, tytuł ksiażki)

Dodanie id książki do indentyfikacji konkretnej ksiązki 
```

class Book:
    def __init__(self, title, author, book_id=None):
        self.id = book_id
        self.title = title
        self.author = author
