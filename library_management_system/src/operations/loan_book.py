import sqlite3
from config import DATABASE

# Function to loan a book
def loan_book(book_id, member_id, due_date):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Check if book is available
    cursor.execute("SELECT IsAvailable FROM Books WHERE BookID = ?", (book_id,))
    result = cursor.fetchone()
    if result and result[0] == 1:
        # Loan the book
        cursor.execute("INSERT INTO Loans (BookID, MemberID, DueDate) VALUES (?, ?, ?)",
                       (book_id, member_id, due_date))
        cursor.execute("UPDATE Books SET IsAvailable = 0 WHERE BookID = ?", (book_id,))
        conn.commit()
        print(f"Book ID {book_id} loaned to Member ID {member_id}")
    else:
        print("Book is not available.")
    
    conn.close()
    # ENDDEF

