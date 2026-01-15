# Łączenie z bazą danych i importowanie pakietów z SQLite3

import sqlite3

DB_NAME = "library.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn