import classes/Library
import classes/Book

# Prosta baza danych na podstawie wywołania klas Library/Book

library = Library()
library.add_book(Book("Pan Tadeusz", "Adam Mickiewicz"))
library.add_book(Book("Quo vadis", "Henryk Siekiewicz"))
library.display_books()

library.add_book(Book(input("Wpisz tytuł ksiązki: "), "Adam Mickiewicz"))
