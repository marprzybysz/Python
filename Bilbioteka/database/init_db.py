# Wywołanie bilbioteki SQLite 3 i stworzenie pierwszej tabeli "books" oraz status ready 

from database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

create_tables()
print("Database ready...")
