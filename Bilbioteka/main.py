import classes/Library
import classes/Book

# Prosta baza danych na podstawie wywołania klas Library/Book

title = input("Wpisz tytuł książki: ")
author = input("Wpisz tytuł autora: ")

library = Library()
library.add_book(Book(title, author))
library.display_books()
