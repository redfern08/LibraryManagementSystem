import sqlite3
from db_setup import load_schema
from operations.add_sample_data import add_sample_data
from operations.loan_book import loan_book
from operations.return_book import return_book

# Display menu options for user
def display_menu():
    print("\nLibrary Management System")
    print("Choose an option below.\n")
    print("1. Set up Database")
    print("2. Add Sample Data")
    print("3. Loan a Book")
    print("4. Return a Book")
    print("5. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                load_schema()
            except sqlite3.OperationalError:
                print("Schema already exists.")
        elif choice == "2":
            try:
                add_sample_data()
            except sqlite3.IntegrityError:
                print("Sample data already exists.")
        elif choice == "3":
            book_id = int(input("Enter Book ID to loan: "))
            member_id = int(input("Enter Member ID: "))
            due_date = input("Enter due date (YYYY-MM-DD): ")
            loan_book(book_id, member_id, due_date)
        elif choice == "4":
            book_id = int(input("Enter Book ID to return: "))
            return_book(book_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
