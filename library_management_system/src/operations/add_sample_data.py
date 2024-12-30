import sqlite3
from config import DATABASE

def add_sample_data():
    # Add intial data to database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Add sample books
    books = [
        ("1984", "George Orwell", "Dystopian"),
        ("To Kill a Mockingbird", "Harper Lee", "Classic"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Genre) VALUES (?, ?, ?)", books)

    # Add sample members
    members = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com")
    ]
    cursor.executemany("INSERT INTO Members (Name, Email) VALUES (?, ?)", members)

    conn.commit()
    conn.close()
    print("Sample data has been added.")
    # ENDDEF


