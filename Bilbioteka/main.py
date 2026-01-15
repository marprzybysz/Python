# Prosta baza danych na podstawie wywołania klas Library/Book

from classes.Library import Library
from classes.Book import Book

title = input("Wpisz tytuł książki: ")
author = input("Wpisz tytuł autora: ")

library = Library()
library.add_book(Book(title, author))
library.display_books()
