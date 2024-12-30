import sqlite3
from config import DATABASE

# Create return book function
def return_book(book_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE Loans SET ReturnDate = DATE('now') WHERE BookID = ? AND ReturnDate IS NULL", (book_id,))
    cursor.execute("UPDATE Books SET IsAvailable = 1 WHERE BookID = ?", (book_id,))
    conn.commit()
    print(f"Book ID {book_id} has been returned")
    # ENDDEF

